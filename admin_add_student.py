from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, ttk, messagebox
import mysql.connector  # pip install mysql-connector-python
import re
import all_credentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def fetch_next_student_id():
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select student_id from " + db_student_table)
        data = cursor.fetchall()
        if len(data) != 0:
            student_id_tuple = []
            for d in data:
                student_id_tuple.append(d[0])
            entry_1.insert(0, student_id_tuple[len(student_id_tuple) - 1] + 1)
        elif len(data) == 0:
            entry_1.insert(0, str(300000 + 1))
        connection.close()
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def validate_all_values():
    email_format_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if student_id.get() == "":
        messagebox.showerror("Error", "Student ID is empty!")
    elif not student_id.get().isdigit():
        messagebox.showerror("Error", "Student ID can be numeric only!")
    elif student_name.get() == "":
        messagebox.showerror("Error", "Student name is empty!")
    elif student_email.get() == "":
        messagebox.showerror("Error", "Student email is empty!")
    elif not re.fullmatch(email_format_regex, student_email.get()):
        messagebox.showerror("Error", "Student email is invalid! Please type a valid email address!")
    elif student_mobile.get() == "":
        messagebox.showerror("Error", "Student Mobile Number is empty!")
    elif not student_mobile.get().isdigit():
        messagebox.showerror("Error", "Mobile Number can be numeric only!")
    elif not len(str(student_mobile.get())) == 10:
        messagebox.showerror("Error", "Mobile Number can have 10 digits only!")
    elif course_selected.get() == "":
        messagebox.showerror("Error", "Course Selected is empty!")
    elif student_gender.get() == "":
        messagebox.showerror("Error", "Gender is empty!")
    elif student_age.get() == "":
        messagebox.showerror("Error", "Student Age is empty!")
    elif residential_address.get() == "":
        messagebox.showerror("Error", "Residential Address is empty!")
    else:
        add_student_to_database()


def add_student_to_database():
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute(
            "insert into " + db_student_table + " values(%s, %s, %s, %s, %s, %s, %s, %s)",
            (student_id.get(),
             student_name.get(),
             student_email.get(),
             student_mobile.get(),
             course_selected.get(),
             student_gender.get(),
             student_age.get(),
             residential_address.get()
             ))
        connection.commit()

        connection.close()
        messagebox.showinfo("Success", "New Student has been Added!", parent=window)
        window.destroy()

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def get_all_course():
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select course_name from " + db_course_table)
        data = cursor.fetchall()

        course_list = ["Not assigned yet"]
        for d in data:
            course_list.append(d[0])

        connection.close()
        return tuple(course_list)
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

# variables
student_id = StringVar()
student_name = StringVar()
student_email = StringVar()
student_mobile = StringVar()
course_selected = StringVar()
student_gender = StringVar()
student_age = StringVar()
residential_address = StringVar()

# Database Connectivity Variables
db_host = all_credentials.host
db_username = all_credentials.username
db_password = all_credentials.password
db_database = all_credentials.database
db_teacher_table = all_credentials.teacher_table_name
db_course_table = all_credentials.course_table_name
db_student_table = all_credentials.student_table_name

window.geometry("720x610")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=610,
    width=720,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    293.0,
    41.0,
    anchor="nw",
    text="Add Student",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    278.0,
    79.0,
    anchor="nw",
    text="Please enter all the details",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_admin_add_student_form_background.png"))
image_1 = canvas.create_image(
    363.0,
    307.0,
    image=image_image_1
)

canvas.create_text(
    122.0,
    142.0,
    anchor="nw",
    text="Student ID : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_1 = canvas.create_image(
    488.5,
    150.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=student_id
)
entry_1.place(
    x=384.0,
    y=136.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    122.0,
    185.0,
    anchor="nw",
    text="Student Name : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_2 = canvas.create_image(
    488.5,
    193.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=student_name
)
entry_2.place(
    x=384.0,
    y=179.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    122.0,
    228.0,
    anchor="nw",
    text="Email Address : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_3 = canvas.create_image(
    488.5,
    236.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=student_email
)
entry_3.place(
    x=384.0,
    y=222.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    122.0,
    271.0,
    anchor="nw",
    text="Mobile Number : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_4 = canvas.create_image(
    488.5,
    279.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=student_mobile
)
entry_4.place(
    x=384.0,
    y=265.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    122.0,
    319.0,
    anchor="nw",
    text="Course Selected : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_5 = canvas.create_image(
    488.5,
    328.0,
    image=entry_image_5
)

course_combo = ttk.Combobox(window,
                            textvariable=course_selected,
                            font=("arial", 10),
                            width=20, state="readonly")
course_combo["value"] = get_all_course()
course_combo.current(0)
course_combo.place(
    x=380.0,
    y=314.0,
    width=220.0,
    height=26.0
)

canvas.create_text(
    122.0,
    369.0,
    anchor="nw",
    text="Gender : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_6 = canvas.create_image(
    488.5,
    377.0,
    image=entry_image_6
)

gender_combo = ttk.Combobox(window,
                            textvariable=student_gender,
                            font=("arial", 10),
                            width=20, state="readonly")
gender_combo["value"] = ("Male",
                         "Female",
                         "Other")
gender_combo.current(0)
gender_combo.place(
    x=380.0,
    y=363.0,
    width=220.0,
    height=26.0
)

canvas.create_text(
    122.0,
    412.0,
    anchor="nw",
    text="Age : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_7 = canvas.create_image(
    488.5,
    420.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=student_age
)
entry_7.place(
    x=384.0,
    y=406.0,
    width=209.0,
    height=26.0
)

canvas.create_text(
    122.0,
    455.0,
    anchor="nw",
    text="Residential Address : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_8 = canvas.create_image(
    488.5,
    463.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=residential_address
)
entry_8.place(
    x=384.0,
    y=449.0,
    width=209.0,
    height=26.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_admin_add_student.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=validate_all_values,
    relief="flat"
)
button_1.place(
    x=293.0,
    y=533.0,
    width=140.0,
    height=39.5604248046875
)

fetch_next_student_id()

window.resizable(False, False)
window.mainloop()
