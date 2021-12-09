from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, messagebox
import mysql.connector  # pip install mysql-connector-python
import all_credentials

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def fetch_course_data(course_id_string):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        cursor = connection.cursor()
        cursor.execute("select * from " + db_course_table + " where course_id=" + str(course_id_string))
        data = cursor.fetchall()

        canvas.itemconfig(course_name_label, text=str(data[0][1]))
        canvas.itemconfig(course_duration_label, text=str(data[0][2]))
        canvas.itemconfig(course_fees_label, text=str(data[0][4]))
        canvas.itemconfig(course_mentor_label, text=str(data[0][6]))
        global course_name
        global course_mentor
        course_name = str(data[0][1])
        course_mentor = str(data[0][6])

    except Exception as es:
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


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


def search_course():
    if course_id.get() == "":
        messagebox.showerror("Error", "Course ID is empty!")
    elif not course_id.get().isdigit():
        messagebox.showerror("Error", "Course ID can be numeric only!")
    elif not is_valid_course_id(course_id.get()):
        messagebox.showerror("Error", "Course ID not valid. Try Again!")
    else:
        messagebox.showerror("Success", "Course ID Found!")
        fetch_course_data(course_id.get())


def remove_course():
    try:
        update = messagebox.askyesno("Update", "Are you sure want to remove this course?", parent=window)
        connection = mysql.connector.connect(host=db_host,
                                             username=db_username,
                                             password=db_password,
                                             database=db_database)
        if update > 0:
            cursor = connection.cursor()

            if course_mentor != "Not assigned yet":
                cursor.execute(
                    "update teachers set course_mentor=%s where teacher_name=%s",
                    ("Not assigned yet",
                     course_mentor,
                     ))

            cursor.execute(
                "delete from courses where course_id=%s",
                (str(course_id.get()),
                 ))
        else:
            if not update:
                return
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Course removed successfully!", parent=window)
        window.destroy()
    except Exception as es:
        print(es)
        messagebox.showerror("Error", f"Due To:{str(es)}", parent=window)


window = Tk()

# variables
course_id = StringVar()
course_name = ""
course_mentor = ""

# Database Connectivity Variables
db_host = all_credentials.host
db_username = all_credentials.username
db_password = all_credentials.password
db_database = all_credentials.database
db_teacher_table = all_credentials.teacher_table_name
db_course_table = all_credentials.course_table_name

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
    34.0,
    anchor="nw",
    text="Remove Course",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    241.0,
    81.0,
    anchor="nw",
    text="Please enter the Course ID to search",
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
    130.0,
    136.0,
    anchor="nw",
    text="Course ID : ",
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
    textvariable=course_id
)
entry_1.place(
    x=223.0,
    y=130.0,
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
    128.0,
    213.0,
    anchor="nw",
    text="Course Name : ",
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

course_name_label = canvas.create_text(
    393.0,
    214.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(
    128.0,
    256.0,
    anchor="nw",
    text="Course Duration : ",
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

course_duration_label = canvas.create_text(
    393.0,
    258.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(
    128.0,
    300.0,
    anchor="nw",
    text="Course Fees : ",
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

course_fees_label = canvas.create_text(
    393.0,
    303.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(
    130.0,
    343.0,
    anchor="nw",
    text="Course Mentor : ",
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

course_mentor_label = canvas.create_text(
    393.0,
    345.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto", 12 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_admin_remove_course.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=remove_course,
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
