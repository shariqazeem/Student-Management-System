from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, ttk, messagebox
import mysql.connector  # pip install mysql-connector-python
import all_credentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def disable_update_form():
    button_2["state"] = "disabled"
    teacher_combo["state"] = "disabled"
    entry_2["state"] = "disabled"
    entry_3["state"] = "disabled"
    entry_4["state"] = "disabled"
    entry_5["state"] = "disabled"
    pass


def enable_update_form():
    button_2["state"] = "normal"
    teacher_combo["state"] = "normal"
    entry_2["state"] = "normal"
    entry_3["state"] = "normal"
    entry_4["state"] = "normal"
    entry_5["state"] = "normal"
    pass


def is_valid_course_id(course_id_string):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select course_id from " + db_course_table)
        data = cursor.fetchall()

        for d in data:
            if course_id_string == str(d[0]):
                return True

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)
    return False


def update_combobox():
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        teacher_list = [str(teacher_combo.get())]
        cursor.execute("select teacher_name from " + db_teacher_table + " where course_mentor='Not assigned yet'")

        data = cursor.fetchall()
        for d in data:
            teacher_list.append(d[0])
        connection.close()
        teacher_combo["value"] = tuple(teacher_list)
        teacher_combo.current(0)
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def fetch_course_data(course_id_string):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select * from " + db_course_table + " where course_id=" + str(course_id_string))
        data = cursor.fetchall()
        print(data[0])

        course_name.set(str(data[0][1]))
        course_duration.set(str(data[0][2]))
        number_of_classes.set(str(data[0][3]))
        total_fees.set(str(data[0][4]))
        mentor.set(str(data[0][6]))
        global previous_mentor
        previous_mentor = str(data[0][6])

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def validate_all_values():
    if course_name.get() == "":
        messagebox.showerror("Error", "Course name is empty!")
    elif course_duration.get() == "":
        messagebox.showerror("Error", "Course duration is empty!")
    elif not course_duration.get().isdigit():
        messagebox.showerror("Error", "Course duration can be numeric only!")
    elif number_of_classes.get() == "":
        messagebox.showerror("Error", "Number of classes is empty!")
    elif not number_of_classes.get().isdigit():
        messagebox.showerror("Error", "Number of classes can be numeric only!")
    elif total_fees.get() == "":
        messagebox.showerror("Error", "Total fees is empty!")
    elif not total_fees.get().isdigit():
        messagebox.showerror("Error", "Total fees can be numeric only!")
    elif mentor.get() == "":
        messagebox.showerror("Error", "Mentor is empty!")
    else:
        update_course_details(course_id.get())


def get_teacher_id(mentor_selected):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        mentor_selected = "'" + mentor_selected + "'"
        cursor.execute("select teacher_id from " + db_teacher_table + " where teacher_name=" + str(mentor_selected))
        data = cursor.fetchall()
        connection.close()
        return str(data[0][0])
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def update_course_details(course_id_string):
    try:
        update = messagebox.askyesno("Update", "Are you sure update this course's details", parent=window)
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        if update > 0:
            cursor = connection.cursor()
            if mentor.get() == "Not assigned yet":
                cursor.execute(
                    "update courses set course_name=%s,course_duration=%s,no_of_classes=%s,total_fees=%s,"
                    "teacher_id=NULL,mentor=%s where course_id=%s",
                    (course_name.get(),
                     course_duration.get(),
                     number_of_classes.get(),
                     total_fees.get(),
                     mentor.get(),
                     course_id_string
                     ))
                cursor.execute(
                    "update teachers set course_mentor=%s where teacher_name=%s",
                    ("Not assigned yet",
                     previous_mentor
                     ))
            elif mentor.get() != "Not assigned yet":
                cursor.execute(
                    "update courses set course_name=%s,course_duration=%s,no_of_classes=%s,total_fees=%s,"
                    "teacher_id=%s,mentor=%s where course_id=%s",
                    (course_name.get(),
                     course_duration.get(),
                     number_of_classes.get(),
                     total_fees.get(),
                     get_teacher_id(mentor.get()),
                     mentor.get(),
                     course_id_string
                     ))
                cursor.execute(
                    "update teachers set course_mentor=%s where teacher_name=%s",
                    (course_name.get(),
                     mentor.get()
                     ))

        else:
            if not update:
                return
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Course details successfully updated", parent=window)
        window.destroy()
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)
    pass


def search_course():
    if course_id.get() == "":
        messagebox.showerror("Error", "Course ID is empty!")
        disable_update_form()
    elif not course_id.get().isdigit():
        messagebox.showerror("Error", "Course ID can be numeric only!")
        disable_update_form()
    elif not is_valid_course_id(course_id.get()):
        messagebox.showerror("Error", "Course ID not valid. Try Again!")
        disable_update_form()
    else:
        messagebox.showerror("Success", "Course ID Found!")
        enable_update_form()
        update_combobox()
        fetch_course_data(course_id.get())


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

# variables
course_id = StringVar()
course_name = StringVar()
course_duration = StringVar()
number_of_classes = StringVar()
total_fees = StringVar()
mentor = StringVar()
previous_mentor = ""

# Database Connectivity Variables
db_host = all_credentials.host
db_username = all_credentials.username
db_password = all_credentials.password
db_database = all_credentials.database
db_teacher_table = all_credentials.teacher_table_name
db_course_table = all_credentials.course_table_name

window.geometry("720x588")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=588,
    width=720,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    285.0,
    35.0,
    anchor="nw",
    text="Update Course",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    262.0,
    72.0,
    anchor="nw",
    text="Please update the course details",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_admin_search_teacher_background.png"))
image_1 = canvas.create_image(
    359.0,
    148.0,
    image=image_image_1
)

canvas.create_text(
    122.0,
    141.0,
    anchor="nw",
    text="Course ID : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_1 = canvas.create_image(
    319.5,
    149.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=course_id
)
entry_1.place(
    x=215.0,
    y=135.0,
    width=209.0,
    height=26.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_admin_search_course.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=search_course,
    relief="flat"
)
button_1.place(
    x=461.0,
    y=135.30770874023438,
    width=140.0,
    height=27.694599151611328
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_admin_update_course_form_background.png"))
image_2 = canvas.create_image(
    359.0,
    324.0,
    image=image_image_2
)

canvas.create_text(
    121.0,
    230.0,
    anchor="nw",
    text="Course Name : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_2 = canvas.create_image(
    487.5,
    238.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=course_name
)
entry_2.place(
    x=383.0,
    y=224.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    121.0,
    273.0,
    anchor="nw",
    text="Duration (months) : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_3 = canvas.create_image(
    487.5,
    281.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=course_duration
)
entry_3.place(
    x=383.0,
    y=267.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    121.0,
    316.0,
    anchor="nw",
    text="Number of Classes : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_4 = canvas.create_image(
    487.5,
    324.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=number_of_classes
)
entry_4.place(
    x=383.0,
    y=310.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    121.0,
    359.0,
    anchor="nw",
    text="Total Fees : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_5 = canvas.create_image(
    487.5,
    367.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=total_fees
)
entry_5.place(
    x=383.0,
    y=353.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    121.0,
    402.0,
    anchor="nw",
    text="Mentor :",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

teacher_combo = ttk.Combobox(window,
                             textvariable=mentor,
                             font=("arial", 10),
                             width=20, state="readonly")
teacher_combo["value"] = ("Not assigned yet",
                          "teacher 1",
                          "teacher 2")
teacher_combo.current(0)
teacher_combo.place(
    x=378.0,
    y=398.0,
    width=220.0,
    height=26.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_admin_update_course.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=validate_all_values,
    relief="flat"
)
button_2.place(
    x=290.0,
    y=500.0,
    width=140.0,
    height=39.5604248046875
)

disable_update_form()

window.resizable(False, False)
window.mainloop()
