from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, messagebox
import mysql.connector  # pip install mysql-connector-python

import all_credentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def is_valid_student_id(student_id_string):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select student_id from " + db_student_table)
        data = cursor.fetchall()

        for d in data:
            if student_id_string == str(d[0]):
                return True

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)
    return False


def fetch_student_data(student_id_string):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select * from " + db_student_table + " where student_id=" + str(student_id_string))
        data = cursor.fetchall()

        canvas.itemconfig(student_name_label, text=str(data[0][1]))
        canvas.itemconfig(student_mobile_label, text=str(data[0][3]))
        canvas.itemconfig(student_email_label, text=str(data[0][2]))
        canvas.itemconfig(course_selected_label, text=str(data[0][4]))

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def search_student():
    if student_id.get() == "":
        messagebox.showerror("Error", "Student ID is empty!")
    elif not student_id.get().isdigit():
        messagebox.showerror("Error", "Student ID can be numeric only!")
    elif not is_valid_student_id(student_id.get()):
        messagebox.showerror("Error", "Student ID not valid. Try Again!")
    else:
        messagebox.showerror("Success", "Student ID Found!")
        fetch_student_data(student_id.get())


def remove_student():
    try:
        update = messagebox.askyesno("Update", "Are you sure want to remove this student?", parent=window)
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        if update > 0:
            cursor = connection.cursor()
            cursor.execute("delete from students where student_id=%s",
                           (str(student_id.get()),
                            ))
        else:
            if not update:
                return
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Student removed successfully!", parent=window)
        window.destroy()
    except Exception as es:
        print(es)
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


window = Tk()

# variables
student_id = StringVar()
student_name = ""
student_mentor = ""

# Database Connectivity Variables
db_host = all_credentials.host
db_username = all_credentials.username
db_password = all_credentials.password
db_database = all_credentials.database
db_teacher_table = all_credentials.teacher_table_name
db_course_table = all_credentials.course_table_name
db_student_table = all_credentials.student_table_name

window.geometry("720x491")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=491,
    width=720,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    280.0,
    33.0,
    anchor="nw",
    text="Remove Student",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    245.0,
    81.0,
    anchor="nw",
    text="Please enter the student ID to search",
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
    128.0,
    136.0,
    anchor="nw",
    text="Student ID : ",
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
    textvariable=student_id
)
entry_1.place(
    x=223.0,
    y=130.0,
    width=209.0,
    height=26.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_admin_search_student.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=search_student,
    relief="flat"
)
button_1.place(
    x=469.0,
    y=129.3100128173828,
    width=140.0,
    height=28.692291259765625
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_admin_remove_teacher_background.png"))
image_2 = canvas.create_image(
    367.0,
    287.0,
    image=image_image_2
)

canvas.create_text(
    126.0,
    213.0,
    anchor="nw",
    text="Student Name : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_rectangle(
    382.0,
    207.0,
    603.0,
    235.0,
    fill="#E9E8E8",
    outline="")

student_name_label = canvas.create_text(
    393.0,
    214.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(
    126.0,
    257.0,
    anchor="nw",
    text="Mobile Number : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_rectangle(
    382.0,
    251.0,
    603.0,
    279.0,
    fill="#E9E8E8",
    outline="")

student_mobile_label = canvas.create_text(
    393.0,
    258.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(
    126.0,
    302.0,
    anchor="nw",
    text="Student Email : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_rectangle(
    383.0,
    295.0,
    603.0,
    323.0,
    fill="#E9E8E8",
    outline="")

student_email_label = canvas.create_text(
    393.0,
    303.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(
    126.0,
    344.0,
    anchor="nw",
    text="Course Selected : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_rectangle(
    383.0,
    338.0,
    604.0,
    366.0,
    fill="#E9E8E8",
    outline="")

course_selected_label = canvas.create_text(
    393.0,
    345.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_admin_remove_student.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=remove_student,
    relief="flat"
)
button_2.place(
    x=289.0,
    y=414.0,
    width=140.0,
    height=40.0
)
window.resizable(False, False)
window.mainloop()
