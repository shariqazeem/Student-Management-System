from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, ttk, messagebox
import re
import mysql.connector  # pip install mysql-connector-python

import all_credentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def validate_all_values():
    email_format_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if teacher_id.get() == "":
        messagebox.showerror("Error", "Teacher ID is empty!")
    elif not teacher_id.get().isdigit():
        messagebox.showerror("Error", "Teacher ID can be numeric only!")
    elif teacher_name.get() == "":
        messagebox.showerror("Error", "Teacher name is empty!")
    elif teacher_email.get() == "":
        messagebox.showerror("Error", "Teacher email is empty!")
    elif not re.fullmatch(email_format_regex, teacher_email.get()):
        messagebox.showerror("Error", "Teacher email is invalid! Please type a valid email address!")
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
    elif teacher_gender.get() == "":
        messagebox.showerror("Error", "Gender is empty!")
    elif teacher_age.get() == "":
        messagebox.showerror("Error", "Teacher Age is empty!")
    elif residential_address.get() == "":
        messagebox.showerror("Error", "Residential Address is empty!")
    else:
        add_teacher_to_database()


def get_available_courses():
    pass


def add_teacher_to_database():
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute(
            "insert into " + db_teacher_table + " values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (teacher_id.get(),
             teacher_name.get(),
             teacher_email.get(),
             teacher_mobile.get(),
             teacher_qualification.get(),
             teaching_subject.get(),
             course_mentor.get(),
             monthly_salary.get(),
             teacher_gender.get(),
             teacher_age.get(),
             residential_address.get()
             ))
        connection.commit()

        connection.close()
        messagebox.showinfo("Success", "New Teacher has been Added!", parent=window)
        window.destroy()

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def fetch_data():
    connection = mysql.connector.connect(host=db_host,
                                         username=db_username,
                                         password=db_password,
                                         database=db_database)
    cursor = connection.cursor()
    cursor.execute("select * from " + db_teacher_table)
    data = cursor.fetchall()
    if len(data) != 0:
        cursor.execute("select teacher_id from " + db_teacher_table + " where teacher_id=" + str(100000 + len(data)))
        data = cursor.fetchall()
        entry_1.insert(0, data[0][0] + 1)
    elif len(data) == 0:
        entry_1.insert(0, str(100000 + 1))
    connection.close()


window = Tk()

# variables
teacher_id = StringVar()
teacher_name = StringVar()
teacher_email = StringVar()
teacher_mobile = StringVar()
teacher_qualification = StringVar()
teaching_subject = StringVar()
course_mentor = StringVar()
monthly_salary = StringVar()
teacher_gender = StringVar()
teacher_age = StringVar()
residential_address = StringVar()

# Database Connectivity Variables
db_host = all_credentials.host
db_username = all_credentials.username
db_password = all_credentials.password
db_database = all_credentials.database
db_teacher_table = all_credentials.teacher_table_name

window.geometry("720x700")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=700,
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
    text="Add Teacher",
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

canvas.create_text(
    121.0,
    134.0,
    anchor="nw",
    text="Teacher ID : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    121.0,
    306.0,
    anchor="nw",
    text="Qualification : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    122.0,
    220.0,
    anchor="nw",
    text="Email Address : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    122.0,
    392.0,
    anchor="nw",
    text="Course Mentor : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    121.0,
    521.0,
    anchor="nw",
    text="Age : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    121.0,
    177.0,
    anchor="nw",
    text="Teacher Name : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    122.0,
    349.0,
    anchor="nw",
    text="Teaching Subject",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    122.0,
    478.0,
    anchor="nw",
    text="Gender : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    122.0,
    263.0,
    anchor="nw",
    text="Mobile Number : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    122.0,
    435.0,
    anchor="nw",
    text="Monthly Salary : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    121.0,
    564.0,
    anchor="nw",
    text="Residential Address : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_1 = canvas.create_image(
    488.5,
    142.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teacher_id
)
entry_1.place(
    x=384.0,
    y=128.0,
    width=209.0,
    height=26.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_2 = canvas.create_image(
    488.5,
    314.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teacher_qualification
)
entry_2.place(
    x=384.0,
    y=300.0,
    width=209.0,
    height=26.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_3 = canvas.create_image(
    488.5,
    228.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teacher_email
)
entry_3.place(
    x=384.0,
    y=214.0,
    width=209.0,
    height=26.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_4 = canvas.create_image(
    488.5,
    529.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teacher_age
)
entry_4.place(
    x=384.0,
    y=515.0,
    width=209.0,
    height=26.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_5 = canvas.create_image(
    488.5,
    185.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teacher_name
)
entry_5.place(
    x=384.0,
    y=171.0,
    width=209.0,
    height=26.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_6 = canvas.create_image(
    488.5,
    357.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teaching_subject
)
entry_6.place(
    x=384.0,
    y=343.0,
    width=209.0,
    height=26.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_7 = canvas.create_image(
    488.5,
    271.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=teacher_mobile
)
entry_7.place(
    x=384.0,
    y=257.0,
    width=209.0,
    height=26.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_8 = canvas.create_image(
    488.5,
    443.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=monthly_salary
)
entry_8.place(
    x=384.0,
    y=429.0,
    width=209.0,
    height=26.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_9 = canvas.create_image(
    488.5,
    572.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=residential_address
)
entry_9.place(
    x=384.0,
    y=558.0,
    width=209.0,
    height=26.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_add_teacher.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=validate_all_values,
    relief="flat"
)
button_1.place(
    x=290.0,
    y=622.5555419921875,
    width=140.0,
    height=40.0
)

gender_combo = ttk.Combobox(window,
                            textvariable=teacher_gender,
                            font=("arial", 10),
                            width=20, state="readonly")
gender_combo["value"] = ("Male",
                         "Female",
                         "Other")
gender_combo.current(0)
gender_combo.place(
    x=380.0,
    y=475.0,
    width=220.0,
    height=26.0
)

course_combo = ttk.Combobox(window,
                            textvariable=course_mentor,
                            font=("arial", 10),
                            width=20, state="readonly")
course_combo["value"] = ("Select Course",
                         "Course 1",
                         "Course 2")
course_combo.current(0)
course_combo.place(
    x=380.0,
    y=386.0,
    width=220.0,
    height=26.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("drop_down_arrow_right.png"))
image_2 = canvas.create_image(
    585.0,
    400.0,
    image=image_image_2
)

fetch_data()

window.resizable(False, False)
window.mainloop()
