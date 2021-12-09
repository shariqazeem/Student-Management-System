from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, messagebox, ttk
import mysql.connector  # pip install mysql-connector-python

import all_credentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def validate_all_values():
    if course_id.get() == "":
        messagebox.showerror("Error", "Course ID is empty!")
    elif not course_id.get().isdigit():
        messagebox.showerror("Error", "Course ID can be numeric only!")
    elif course_name.get() == "":
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
        add_course()


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


def add_course():
    mentor_selected = mentor.get()
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute(
            "insert into " + db_course_table + " values(%s, %s, %s, %s, %s, NULL, %s)",
            (course_id.get(),
             course_name.get(),
             course_duration.get(),
             number_of_classes.get(),
             total_fees.get(),
             mentor.get()
             ))
        connection.commit()

        if mentor_selected != "Not assigned yet":
            teacher_id = get_teacher_id(mentor_selected)

            cursor.execute(
                "update courses set teacher_id=%s where mentor=%s",
                (str(teacher_id),
                 str(mentor_selected)
                 ))
            connection.commit()
            cursor.execute(
                "update teachers set course_mentor=%s where teacher_id=%s",
                (course_name.get(),
                 str(teacher_id)
                 ))
            connection.commit()

        connection.close()
        messagebox.showinfo("Success", "New Course has been Added!", parent=window)
        window.destroy()

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def get_all_available_teacher():
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select teacher_name from " + db_teacher_table + " where course_mentor='Not assigned yet'")
        data = cursor.fetchall()

        teacher_list = ["Not assigned yet"]
        for d in data:
            teacher_list.append(d[0])

        connection.close()
        return tuple(teacher_list)
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def fetch_next_course_id():
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select course_id from " + db_course_table)
        data = cursor.fetchall()

        if len(data) != 0:
            course_id_tuple = []
            for d in data:
                course_id_tuple.append(d[0])
            print()
            entry_1.insert(0, course_id_tuple[len(course_id_tuple) - 1] + 1)
        elif len(data) == 0:
            entry_1.insert(0, str(200000 + 1))
        connection.close()
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


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

# Database Connectivity Variables
db_host = all_credentials.host
db_username = all_credentials.username
db_password = all_credentials.password
db_database = all_credentials.database
db_teacher_table = all_credentials.teacher_table_name
db_course_table = all_credentials.course_table_name

window.geometry("720x548")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=548,
    width=720,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    301.0,
    34.00000000000006,
    anchor="nw",
    text="Add Course",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    282.0,
    78.00000000000006,
    anchor="nw",
    text="Please enter all the details",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_admin_add_course_form_background.png"))
image_1 = canvas.create_image(
    359.0,
    288.00000000000006,
    image=image_image_1
)

canvas.create_text(
    121.0,
    173.00000000000006,
    anchor="nw",
    text="Course ID : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_1 = canvas.create_image(
    487.5,
    181.00000000000006,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=course_id
)
entry_1.place(
    x=383.0,
    y=167.00000000000006,
    width=209.0,
    height=26.0
)

canvas.create_text(
    121.0,
    216.00000000000006,
    anchor="nw",
    text="Course Name : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_2 = canvas.create_image(
    487.5,
    224.00000000000006,
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
    y=210.00000000000006,
    width=209.0,
    height=26.0
)

canvas.create_text(
    121.0,
    259.00000000000006,
    anchor="nw",
    text="Duration (months) : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_3 = canvas.create_image(
    487.5,
    267.00000000000006,
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
    y=253.00000000000006,
    width=209.0,
    height=26.0
)

canvas.create_text(
    121.0,
    302.00000000000006,
    anchor="nw",
    text="Number of Classes : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_4 = canvas.create_image(
    487.5,
    310.00000000000006,
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
    y=296.00000000000006,
    width=209.0,
    height=26.0
)

canvas.create_text(
    121.0,
    345.00000000000006,
    anchor="nw",
    text="Total Fees : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_5 = canvas.create_image(
    487.5,
    353.00000000000006,
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
    y=339.00000000000006,
    width=209.0,
    height=26.0
)

canvas.create_text(
    121.0,
    388.00000000000006,
    anchor="nw",
    text="Mentor :",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

teacher_combo = ttk.Combobox(window,
                             textvariable=mentor,
                             font=("arial", 10),
                             width=20, state="readonly")
teacher_combo["value"] = get_all_available_teacher()
teacher_combo.current(0)
teacher_combo.place(
    x=378.0,
    y=382.0,
    width=220.0,
    height=26.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_admin_add_course.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=validate_all_values,
    relief="flat"
)
button_1.place(
    x=294.0,
    y=469.00000000000006,
    width=140.0,
    height=39.5604248046875
)

fetch_next_course_id()

window.resizable(False, False)
window.mainloop()
