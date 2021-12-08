from pathlib import Path
import mysql.connector  # pip install mysql-connector-python
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, messagebox

import all_credentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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

        canvas.itemconfig(teacher_name_label, text=str(data[0][1]))
        canvas.itemconfig(teacher_mobile_label, text=str(data[0][3]))
        canvas.itemconfig(course_mentor_label, text=str(data[0][6]))
        canvas.itemconfig(monthly_salary_label, text=str(data[0][7]))

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def get_previous_teacher_course(teacher_id_string):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select course_mentor from " + db_teacher_table + " where teacher_id=" + str(teacher_id_string))
        data = cursor.fetchall()
        connection.close()
        return data[0][0]
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)
    pass


def search_teacher():
    if teacher_id.get() == "":
        messagebox.showerror("Error", "Teacher ID is empty!")
    elif not teacher_id.get().isdigit():
        messagebox.showerror("Error", "Teacher ID can be numeric only!")
    elif not is_valid_teacher_id(teacher_id.get()):
        messagebox.showerror("Error", "Teacher ID not valid. Try Again!")
    else:
        messagebox.showerror("Success", "Teacher ID Found!")
        fetch_teacher_data(teacher_id.get())


def remove_teacher():
    previous_course = get_previous_teacher_course(teacher_id.get())
    print(previous_course)
    try:
        update = messagebox.askyesno("Update", "Are you sure want to remove this teacher?", parent=window)
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        if update > 0:
            cursor = connection.cursor()

            cursor.execute(
                "delete from teachers where teacher_id=%s",
                (str(teacher_id.get()),
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
        messagebox.showinfo("Success", "Teacher removed successfully!", parent=window)
        window.destroy()
    except Exception as es:
        print(es)
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


window = Tk()

teacher_id = StringVar()

# Database Connectivity Variables
db_host = all_credentials.host
db_username = all_credentials.username
db_password = all_credentials.password
db_database = all_credentials.database
db_teacher_table = all_credentials.teacher_table_name


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
    270.0,
    33.99999999999994,
    anchor="nw",
    text="Remove Teacher",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    240.0,
    80.99999999999994,
    anchor="nw",
    text="Please enter the teacher ID to search",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_admin_search_teacher_background.png"))
image_1 = canvas.create_image(
    367.0,
    142.99999999999994,
    image=image_image_1
)

canvas.create_text(
    127.0,
    135.99999999999994,
    anchor="nw",
    text="Teacher ID : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_1 = canvas.create_image(
    327.5,
    143.99999999999994,
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
    y=129.99999999999994,
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
    y=129.31001281738276,
    width=140.0,
    height=28.692291259765625
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_admin_remove_teacher_background.png"))
image_2 = canvas.create_image(
    367.0,
    286.99999999999994,
    image=image_image_2
)

canvas.create_text(
    125.0,
    212.99999999999994,
    anchor="nw",
    text="Teacher Name : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_rectangle(
    382.0,
    206.99999999999994,
    603.0,
    234.99999999999994,
    fill="#E9E8E8",
    outline="")

teacher_name_label = canvas.create_text(
    393.0,
    213.99999999999994,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(
    126.0,
    256.99999999999994,
    anchor="nw",
    text="Mobile Number : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_rectangle(
    382.0,
    250.99999999999994,
    603.0,
    278.99999999999994,
    fill="#E9E8E8",
    outline="")

teacher_mobile_label = canvas.create_text(
    393.0,
    257.99999999999994,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(
    127.0,
    300.99999999999994,
    anchor="nw",
    text="Course Mentor : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_rectangle(
    383.0,
    294.99999999999994,
    603.0,
    322.99999999999994,
    fill="#E9E8E8",
    outline="")

course_mentor_label = canvas.create_text(
    393.0,
    302.99999999999994,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(
    127.0,
    343.99999999999994,
    anchor="nw",
    text="Monthly Salary : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_rectangle(
    383.0,
    337.99999999999994,
    604.0,
    365.99999999999994,
    fill="#E9E8E8",
    outline="")

monthly_salary_label = canvas.create_text(
    393.0,
    344.99999999999994,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_admin_remove_teacher.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=remove_teacher,
    relief="flat"
)
button_2.place(
    x=289.0,
    y=413.99999999999994,
    width=140.0,
    height=40.0
)
window.resizable(False, False)
window.mainloop()
