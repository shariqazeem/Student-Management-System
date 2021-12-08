from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, Frame, ttk, VERTICAL, HORIZONTAL, BOTTOM, RIGHT, X, Y, BOTH, StringVar, END, \
    Button, messagebox
import mysql.connector  # pip install mysql-connector-python

import all_credentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def close_window():
    close = messagebox.askyesno("Update", "Are you sure want to close this window?", parent=window)
    if close > 0:
        window.destroy()
    else:
        if not close:
            return


# fetch function
def fetch_data():
    connection = mysql.connector.connect(host=db_host,
                                         username=db_username,
                                         password=db_password,
                                         database=db_database)
    cursor = connection.cursor()
    cursor.execute("select * from teachers")
    data = cursor.fetchall()
    if len(data) != 0:
        student_table.delete(*student_table.get_children())
        for i in data:
            student_table.insert("", END, values=i)
        connection.commit()
    connection.close()


def get_cursor(event=""):
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    data = content["values"]

    teacher_id.set(data[0])
    teacher_name.set(data[1])
    teacher_email.set(data[2])
    teacher_mobile.set(data[3])
    teacher_qualification.set(data[4])
    teaching_subject.set(data[5])
    course_mentor.set(data[6])
    monthly_salary.set(data[7])
    teacher_gender.set(data[8])
    teacher_age.set(data[9])
    residential_address.set(data[10])


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

window.geometry("960x491")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=491,
    width=960,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    395.0,
    29.0,
    anchor="nw",
    text="All Teachers",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    368.0,
    67.0,
    anchor="nw",
    text="Below is the all teacher data in table",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_close.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=close_window,
    relief="flat"
)
button_1.place(
    x=51.0,
    y=35.0,
    width=53.0,
    height=32.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_admin_show_all_teacher.png"))
image_1 = canvas.create_image(
    477.0,
    279.0,
    image=image_image_1
)

# Student Table & scroll bar
table_frame = Frame(window, bd=4, relief="ridge")
table_frame.place(x=51, y=112, width=852, height=335)

scroll_bar_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
scroll_bar_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
student_table = ttk.Treeview(table_frame, column=("teacher_id",
                                                  "teacher_name",
                                                  "teacher_email",
                                                  "teacher_mobile",
                                                  "teacher_qualification",
                                                  "teaching_subject",
                                                  "course_mentor",
                                                  "monthly_salary",
                                                  "gender",
                                                  "age",
                                                  "residential_address"),
                             xscrollcommand=scroll_bar_x.set,
                             yscrollcommand=scroll_bar_y.set)
scroll_bar_x.pack(side=BOTTOM, fill=X)
scroll_bar_y.pack(side=RIGHT, fill=Y)

scroll_bar_x.config(command=student_table.xview)
scroll_bar_y.config(command=student_table.yview)

student_table.heading("teacher_id", text="Teacher ID")
student_table.heading("teacher_name", text="Teacher Name")
student_table.heading("teacher_email", text="Teacher Email")
student_table.heading("teacher_mobile", text="Teacher Mobile")
student_table.heading("teacher_qualification", text="Teacher Qualification")
student_table.heading("teaching_subject", text="Teaching Subject")
student_table.heading("course_mentor", text="Course Mentor")
student_table.heading("monthly_salary", text="monthly Salary")
student_table.heading("gender", text="Gender")
student_table.heading("age", text="age")
student_table.heading("residential_address", text="Residential Address")

student_table["show"] = "headings"

student_table.column("teacher_id", width=100)
student_table.column("teacher_name", width=150)
student_table.column("teacher_email", width=200)
student_table.column("teacher_mobile", width=150)
student_table.column("teacher_qualification", width=200)
student_table.column("teaching_subject", width=200)
student_table.column("course_mentor", width=200)
student_table.column("monthly_salary", width=100)
student_table.column("gender", width=100)
student_table.column("age", width=100)
student_table.column("residential_address", width=500)

student_table.pack(fill=BOTH, expand=1)
student_table.bind("<ButtonRelease>", get_cursor)
fetch_data()

window.resizable(False, False)
window.mainloop()
