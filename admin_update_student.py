from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, messagebox
import mysql.connector  # pip install mysql-connector-python
import all_credentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def disable_update_form():
    button_2["state"] = "disabled"
    entry_2["state"] = "disabled"
    entry_3["state"] = "disabled"
    entry_4["state"] = "disabled"
    entry_5["state"] = "disabled"
    entry_6["state"] = "disabled"
    pass


def enable_update_form():
    button_2["state"] = "normal"
    entry_3["state"] = "normal"
    entry_5["state"] = "normal"
    entry_6["state"] = "normal"
    pass


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
        print(data[0])

        student_name.set(str(data[0][1]))
        student_mobile.set(str(data[0][3]))
        course_selected.set(str(data[0][4]))
        student_age.set(str(data[0][6]))
        residential_address.set(str(data[0][7]))

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def search_student():
    if student_id.get() == "":
        messagebox.showerror("Error", "Student ID is empty!")
        disable_update_form()
    elif not student_id.get().isdigit():
        messagebox.showerror("Error", "Student ID can be numeric only!")
        disable_update_form()
    elif not is_valid_student_id(student_id.get()):
        messagebox.showerror("Error", "Student ID not valid. Try Again!")
        disable_update_form()
    else:
        messagebox.showerror("Success", "Student ID Found!")
        enable_update_form()
        fetch_student_data(student_id.get())


def update_student_details(student_id_string):
    try:
        update = messagebox.askyesno("Update", "Are you sure update this student's details", parent=window)
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        if update > 0:
            cursor = connection.cursor()
            cursor.execute(
                "update students set student_mobile=%s,student_age=%s,residential_address=%s where student_id=%s",
                (student_mobile.get(),
                 student_age.get(),
                 residential_address.get(),
                 str(student_id_string)
                 ))
        else:
            if not update:
                return
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Students details successfully updated", parent=window)
        window.destroy()
    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


def validate_all_values():
    if student_mobile.get() == "":
        messagebox.showerror("Error", "Student Mobile Number is empty!")
    elif not student_mobile.get().isdigit():
        messagebox.showerror("Error", "Mobile Number can be numeric only!")
    elif not len(str(student_mobile.get())) == 10:
        messagebox.showerror("Error", "Mobile Number can have 10 digits only!")
    elif student_age.get() == "":
        messagebox.showerror("Error", "Student Age is empty!")
    elif not student_age.get().isdigit():
        messagebox.showerror("Error", "Student Age can be numeric only!")
    elif residential_address.get() == "":
        messagebox.showerror("Error", "Residential Address is empty!")
    else:
        update_student_details(student_id.get())


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

# variables
student_id = StringVar()
student_name = StringVar()
student_mobile = StringVar()
course_selected = StringVar()
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

window.geometry("720x540")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=540,
    width=720,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    236.0,
    33.99999999999994,
    anchor="nw",
    text="Update Student Details",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    281.0,
    76.99999999999994,
    anchor="nw",
    text="Please update the details",
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
    128.0,
    135.99999999999994,
    anchor="nw",
    text="Student ID : ",
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
    textvariable=student_id
)
entry_1.place(
    x=223.0,
    y=129.99999999999994,
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
    y=130.30770874023432,
    width=140.0,
    height=27.694595336914062
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_admin_update_course_form_background.png"))
image_2 = canvas.create_image(
    367.0,
    309.99999999999994,
    image=image_image_2
)

canvas.create_text(
    126.0,
    212.99999999999994,
    anchor="nw",
    text="Student Name : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_2 = canvas.create_image(
    492.5,
    220.99999999999994,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=student_name
)
entry_2.place(
    x=388.0,
    y=206.99999999999994,
    width=209.0,
    height=26.0
)

canvas.create_text(
    126.0,
    256.99999999999994,
    anchor="nw",
    text="Mobile Number : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_3 = canvas.create_image(
    492.5,
    264.99999999999994,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=student_mobile
)
entry_3.place(
    x=388.0,
    y=250.99999999999994,
    width=209.0,
    height=26.0
)

canvas.create_text(
    126.0,
    299.99999999999994,
    anchor="nw",
    text="Course Selected : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_4 = canvas.create_image(
    492.5,
    307.99999999999994,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=course_selected
)
entry_4.place(
    x=388.0,
    y=293.99999999999994,
    width=209.0,
    height=26.0
)

canvas.create_text(
    128.0,
    342.99999999999994,
    anchor="nw",
    text="Age : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_5 = canvas.create_image(
    492.5,
    350.99999999999994,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=student_age
)
entry_5.place(
    x=388.0,
    y=336.99999999999994,
    width=209.0,
    height=26.0
)

canvas.create_text(
    126.0,
    386.99999999999994,
    anchor="nw",
    text="Residential Address : ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_admin_add_teacher_textbox.png"))
entry_bg_6 = canvas.create_image(
    493.5,
    394.99999999999994,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=residential_address
)
entry_6.place(
    x=389.0,
    y=380.99999999999994,
    width=209.0,
    height=26.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_admin_update_student.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=validate_all_values,
    relief="flat"
)
button_2.place(
    x=289.0,
    y=461.99999999999994,
    width=140.0,
    height=40.0
)

disable_update_form()

window.resizable(False, False)
window.mainloop()
