from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, Frame, ttk, VERTICAL, HORIZONTAL, BOTTOM, \
    RIGHT, X, Y, BOTH, StringVar, END, Button, messagebox
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


def fetch_data():
    connection = mysql.connector.connect(host=db_host,
                                         username=db_username,
                                         password=db_password,
                                         database=db_database)
    cursor = connection.cursor()
    cursor.execute("select * from courses")
    data = cursor.fetchall()
    if len(data) != 0:
        course_table.delete(*course_table.get_children())
        for i in data:
            course_table.insert("", END, values=i)
        connection.commit()
    connection.close()


def get_cursor(event=""):
    cursor_row = course_table.focus()
    content = course_table.item(cursor_row)
    data = content["values"]

    course_id.set(data[0])
    course_name.set(data[1])
    course_duration.set(data[2])
    no_of_classes.set(data[3])
    total_fees.set(data[4])
    teacher_id.set(data[5])
    mentor.set(data[6])


window = Tk()

# variables
course_id = StringVar()
course_name = StringVar()
course_duration = StringVar()
no_of_classes = StringVar()
total_fees = StringVar()
teacher_id = StringVar()
mentor = StringVar()

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
course_table = ttk.Treeview(table_frame, column=("course_id",
                                                 "course_name",
                                                 "course_duration",
                                                 "no_of_classes",
                                                 "total_fees",
                                                 "teacher_id",
                                                 "mentor"),
                            xscrollcommand=scroll_bar_x.set,
                            yscrollcommand=scroll_bar_y.set)
scroll_bar_x.pack(side=BOTTOM, fill=X)
scroll_bar_y.pack(side=RIGHT, fill=Y)

scroll_bar_x.config(command=course_table.xview)
scroll_bar_y.config(command=course_table.yview)

course_table.heading("course_id", text="Course ID")
course_table.heading("course_name", text="Course Name")
course_table.heading("course_duration", text="Course Duration")
course_table.heading("no_of_classes", text="Numbers of Classes")
course_table.heading("total_fees", text="Total Fees")
course_table.heading("teacher_id", text="Teacher ID")
course_table.heading("mentor", text="Course Mentor")

course_table["show"] = "headings"

course_table.column("course_id", width=100)
course_table.column("course_name", width=150)
course_table.column("course_duration", width=50)
course_table.column("no_of_classes", width=50)
course_table.column("total_fees", width=100)
course_table.column("teacher_id", width=100)
course_table.column("mentor", width=150)

course_table.pack(fill=BOTH, expand=1)
course_table.bind("<ButtonRelease>", get_cursor)
fetch_data()

window.resizable(False, False)
window.mainloop()
