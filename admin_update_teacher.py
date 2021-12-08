from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, StringVar, messagebox
import mysql.connector  # pip install mysql-connector-python
import all_credentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def disable_update_form():
    button_2["state"] = "disabled"
    course_combo["state"] = "disabled"
    entry_2["state"] = "disabled"
    entry_3["state"] = "disabled"
    entry_4["state"] = "disabled"
    entry_5["state"] = "disabled"
    entry_7["state"] = "disabled"
    entry_8["state"] = "disabled"
    pass


def enable_update_form():
    button_2["state"] = "normal"
    course_combo["state"] = "normal"
    #entry_2["state"] = "normal"
    entry_3["state"] = "normal"
    entry_4["state"] = "normal"
    entry_5["state"] = "normal"
    entry_7["state"] = "normal"
    entry_8["state"] = "normal"
    pass


def is_valid_teacher_id(teacher_id_string):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select teacher_id from " + db_teacher_table)
        data = cursor.fetchall()

        for d in data:
            if teacher_id_string == str(d[0]):
                return True

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)
    return False


def fetch_teacher_data(teacher_id_string):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select * from " + db_teacher_table + " where teacher_id=" + str(teacher_id_string))
        data = cursor.fetchall()
        print(data[0])

        teacher_name.set(str(data[0][1]))
        teacher_mobile.set(str(data[0][3]))
        teacher_qualification.set(str(data[0][4]))
        teaching_subject.set(str(data[0][5]))
        course_mentor.set(data[0][6])
        monthly_salary.set(str(data[0][7]))
        residential_address.set(str(data[0][10]))

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def update_combobox():
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        course_list = [str(course_combo.get())]
        cursor.execute("select course_name from " + db_course_table + " where teacher_id IS NULL")

        data = cursor.fetchall()
        for d in data:
            course_list.append(d[0])
        connection.close()
        course_combo["value"] = tuple(course_list)
        course_combo.current(0)
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def search_teacher():
    if teacher_id.get() == "":
        messagebox.showerror("Error", "Teacher ID is empty!")
        disable_update_form()
    elif not teacher_id.get().isdigit():
        messagebox.showerror("Error", "Teacher ID can be numeric only!")
        disable_update_form()
    elif not is_valid_teacher_id(teacher_id.get()):
        messagebox.showerror("Error", "Teacher ID not valid. Try Again!")
        disable_update_form()
    else:
        messagebox.showerror("Success", "Teacher ID Found!")
        enable_update_form()
        update_combobox()
        fetch_teacher_data(teacher_id.get())


def validate_all_values():
    if teacher_name.get() == "":
        messagebox.showerror("Error", "Teacher name is empty!")
    elif teacher_mobile.get() == "":
        messagebox.showerror("Error", "Teacher Mobile Number is empty!")
    elif not teacher_mobile.get().isdigit():
        messagebox.showerror("Error", "Mobile Number can be numeric only!")
    elif not len(str(teacher_mobile.get())) == 10:
        messagebox.showerror("Error", "Mobile Number can have 10 digits only!")
    elif teacher_qualification.get() == "":
        messagebox.showerror("Error", "Qualification is empty!")
    elif teaching_subject.get() == "":
        messagebox.showerror("Error", "Teacher Subject is empty!")
    elif course_mentor.get() == "":
        messagebox.showerror("Error", "Course is empty!")
    elif monthly_salary.get() == "":
        messagebox.showerror("Error", "Monthly Salary is empty!")
    elif residential_address.get() == "":
        messagebox.showerror("Error", "Residential Address is empty!")
    else:
        update_teacher_details(teacher_id.get())


def get_previous_teacher_course(teacher_id_string):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select course_name from " + db_course_table + " where teacher_id=" + str(teacher_id_string))
        data = cursor.fetchall()
        connection.close()
        return data[0][0]
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)
    pass


def get_all_available_course():
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        print(teacher_id.get())
        cursor.execute("select course_name from " + db_course_table + " where teacher_id=" + str(teacher_id.get()))
        data = cursor.fetchall()
        print(data)
        course_list = [course_combo.get()]
        for d in data:
            course_list.append(d[0])

        connection.close()
        return tuple(course_list)
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def update_teacher_details(teacher_id_string):
    previous_course = get_previous_teacher_course(teacher_id_string)
    try:
        update = messagebox.askyesno("Update", "Are you sure update this teacher's details", parent=window)
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        if update > 0:
            cursor = connection.cursor()
            cursor.execute(
                "update teachers set teacher_name=%s,teacher_mobile=%s,teacher_qualification=%s,teaching_subject=%s,"
                "course_mentor=%s,monthly_salary=%s,residential_address=%s where teacher_id=%s",
                (teacher_name.get(),
                 teacher_mobile.get(),
                 teacher_qualification.get(),
                 teaching_subject.get(),
                 course_mentor.get(),
                 monthly_salary.get(),
                 residential_address.get(),
                 str(teacher_id_string)
                 ))
            cursor.execute(
                "update courses set teacher_id=%s,mentor=%s where course_name=%s",
                (teacher_id.get(),
                 teacher_name.get(),
                 course_mentor.get(),
                 ))
            cursor.execute(
                "update courses set teacher_id=NULL,mentor=%s where course_name=%s",
                ("Not assigned yet",
                 previous_course,
                 ))
        else:
            if not update:
                return
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Teacher details successfully updated", parent=window)
        window.destroy()
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


window = Tk()

# variables
teacher_id = StringVar()
teacher_name = StringVar()
teacher_mobile = StringVar()
teacher_qualification = StringVar()
teaching_subject = StringVar()
course_mentor = StringVar()
monthly_salary = StringVar()
residential_address = StringVar()

# Database Connectivity Variables
db_host = all_credentials.host
db_username = all_credentials.username
db_password = all_credentials.password
db_database = all_credentials.database
db_teacher_table = all_credentials.teacher_table_name
db_course_table = all_credentials.course_table_name

window.geometry("720x613")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=613,
    width=720,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    236.0,
    34.0,
    anchor="nw",
    text="Update Teacher Details",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    281.0,
    77.0,
    anchor="nw",
    text="Please update the details",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_admin_search_teacher_background.png"))
image_1 = canvas.create_image(
    367.0,
    143.0,
    image=image_image_1
)

canvas.create_text(
    127.0,
    136.0,
    anchor="nw",
    text="Teacher ID : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_1 = canvas.create_image(
    327.5,
    144.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teacher_id
)
entry_1.place(
    x=223.0,
    y=130.0,
    width=209.0,
    height=26.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_admin_search_teacher.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=search_teacher,
    relief="flat"
)
button_1.place(
    x=469.0,
    y=130.30770874023438,
    width=140.0,
    height=27.694610595703125
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_admin_update_teacher.png"))
image_2 = canvas.create_image(
    367.0,
    351.0,
    image=image_image_2
)

label1 = canvas.create_text(
    125.0,
    213.0,
    anchor="nw",
    text="Teacher Name : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_2 = canvas.create_image(
    492.5,
    221.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teacher_name
)
entry_2.place(
    x=388.0,
    y=207.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    126.0,
    257.0,
    anchor="nw",
    text="Mobile Number : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_3 = canvas.create_image(
    492.5,
    265.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teacher_mobile
)
entry_3.place(
    x=388.0,
    y=251.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    125.0,
    300.0,
    anchor="nw",
    text="Qualification : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_4 = canvas.create_image(
    492.5,
    308.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teacher_qualification
)
entry_4.place(
    x=388.0,
    y=294.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    126.0,
    343.0,
    anchor="nw",
    text="Teaching Subject",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_5 = canvas.create_image(
    492.5,
    351.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teaching_subject
)
entry_5.place(
    x=388.0,
    y=337.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    126.0,
    386.0,
    anchor="nw",
    text="Course Mentor : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

course_combo = ttk.Combobox(window,
                            textvariable=course_mentor,
                            font=("arial", 10),
                            width=20, state="readonly")
course_combo["value"] = ("Not assigned yet",
                         "course 1",
                         "course2")

course_combo.current(0)
course_combo.place(
    x=383.0,
    y=380.0,
    width=220.0,
    height=26.0
)

canvas.create_text(
    126.0,
    429.0,
    anchor="nw",
    text="Monthly Salary : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_7 = canvas.create_image(
    492.5,
    437.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=monthly_salary
)
entry_7.place(
    x=388.0,
    y=423.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    125.0,
    472.0,
    anchor="nw",
    text="Residential Address : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_8 = canvas.create_image(
    492.5,
    480.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=residential_address
)
entry_8.place(
    x=388.0,
    y=466.0,
    width=209.0,
    height=26.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_admin_update_teacher.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=validate_all_values,
    relief="flat"
)
button_2.place(
    x=290.0,
    y=536.0,
    width=140.0,
    height=40.0
)

disable_update_form()

window.resizable(False, False)
window.mainloop()
