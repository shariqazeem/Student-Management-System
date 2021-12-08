from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def update_student_data():
    print("update student data")


def update_attendance():
    print("update attendance")


def show_all_students():
    print("show all students")


def add_assignment():
    print("add assignment")


def update_assignment():
    print("update assignment")


def update_assignment_marks():
    print("update assignment marks")


def open_notice_board():
    print("open_notice_board")


def add_final_exam():
    print("Add Exam")


def update_exam_marks():
    print("update exam marks")


window = Tk()

# variables
teacher_name = "Subhashree Bhattacharya"
teacher_id = "20012334"

window.geometry("720x480")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=480,
    width=720,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    235.0,
    47.0,
    anchor="nw",
    text="Teacher - Home Screen",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_teacher_name_id_background.png"))
image_1 = canvas.create_image(
    360.0,
    127.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_button_background.png"))
image_2 = canvas.create_image(
    359.0,
    298.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_button_background.png"))
image_3 = canvas.create_image(
    155.0,
    298.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_button_background.png"))
image_4 = canvas.create_image(
    563.0,
    298.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_student_data.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=update_student_data,
    relief="flat"
)
button_1.place(
    x=91.0,
    y=235.0,
    width=130.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_add.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=add_assignment,
    relief="flat"
)
button_2.place(
    x=295.0,
    y=235.0,
    width=130.0,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_notice.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_notice_board,
    relief="flat"
)
button_3.place(
    x=499.0,
    y=235.0,
    width=130.0,
    height=40.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_attendance.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=update_attendance,
    relief="flat"
)
button_4.place(
    x=91.0,
    y=292.0,
    width=130.0,
    height=40.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_update_assignment.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=update_assignment,
    relief="flat"
)
button_5.place(
    x=295.0,
    y=292.0,
    width=130.0,
    height=40.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_exam.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=add_final_exam,
    relief="flat"
)
button_6.place(
    x=499.0,
    y=292.0,
    width=130.0,
    height=40.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_show_all_students.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=show_all_students,
    relief="flat"
)
button_7.place(
    x=91.0,
    y=349.0,
    width=130.0,
    height=40.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_assignment_marks.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=update_assignment_marks,
    relief="flat"
)
button_8.place(
    x=295.0,
    y=349.0,
    width=130.0,
    height=40.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_exam_marks.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=update_exam_marks,
    relief="flat"
)
button_9.place(
    x=499.0,
    y=349.0,
    width=130.0,
    height=40.0
)

canvas.create_text(
    129.0,
    203.0,
    anchor="nw",
    text="Updates",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    318.0,
    203.0,
    anchor="nw",
    text="Assignments",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    529.0,
    203.0,
    anchor="nw",
    text="Final Exam",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    135.0,
    119.0,
    anchor="nw",
    text="Teacher Name : " + teacher_name,
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    443.0,
    119.0,
    anchor="nw",
    text="Teacher ID : " + teacher_id,
    fill="#000000",
    font=("Roboto", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
