from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def open_notice_board():
    print("open_notice_board")


def show_performance():
    print("show performance")


def show_payment_statements():
    print("show payment statement")


def show_enrolled_course_details():
    print("show enrolled course details")


def show_and_submit_assignment():
    print("show and submit assignment")


def show_and_submit_final_exam():
    print("show and submit final exam")


window = Tk()

# variables
student_name = "Joy Kishan Sharma"
student_id = "2771234"

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
    text="Student - Home Screen",
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
    file=relative_to_assets("image_button_background_student.png"))
image_2 = canvas.create_image(
    497.0,
    298.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_button_background_student.png"))
image_3 = canvas.create_image(
    223.0,
    298.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_notice_board_student.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_notice_board,
    relief="flat"
)
button_1.place(
    x=145.0,
    y=235.0,
    width=158.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_course_enrolled.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=show_enrolled_course_details,
    relief="flat"
)
button_2.place(
    x=419.0,
    y=235.0,
    width=158.0,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_show_performance.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=show_performance,
    relief="flat"
)
button_3.place(
    x=145.0,
    y=292.0,
    width=158.0,
    height=40.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_assignment_student.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=show_and_submit_assignment,
    relief="flat"
)
button_4.place(
    x=419.0,
    y=292.0,
    width=158.0,
    height=40.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_payment_statement_student.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=show_payment_statements,
    relief="flat"
)
button_5.place(
    x=145.0,
    y=349.0,
    width=158.0,
    height=40.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_final_exam_student.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=show_and_submit_final_exam,
    relief="flat"
)
button_6.place(
    x=419.0,
    y=349.0,
    width=158.0,
    height=40.0
)

canvas.create_text(
    164.0,
    203.0,
    anchor="nw",
    text="Show Information",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    444.0,
    203.0,
    anchor="nw",
    text="Course Materials",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    140.0,
    119.0,
    anchor="nw",
    text="Student Name : " + student_name,
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    443.0,
    119.0,
    anchor="nw",
    text="Student ID : " + student_id,
    fill="#000000",
    font=("Roboto", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
