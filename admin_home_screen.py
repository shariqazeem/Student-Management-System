import os
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def add_teacher():
    os.system('python admin_add_teacher.py')
    pass


def update_teacher_data():
    os.system('python admin_update_teacher.py')
    pass


def remove_teacher():
    os.system('python admin_remove_teacher.py')
    pass


def show_all_teacher():
    os.system('python admin_show_all_teachers.py')
    pass


def add_course():
    os.system('python admin_add_course.py')
    pass


def update_course_data():
    os.system('python admin_update_course.py')
    pass


def remove_course():
    os.system('python admin_remove_course.py')
    pass


def show_all_course():
    os.system('python admin_show_all_courses.py')
    pass


def add_student():
    print("add student")
    pass


def update_student_data():
    print("update student")
    pass


def remove_student():
    print("remove student")
    pass


def show_all_student():
    print("show all student")
    pass


def open_student_payment():
    print("open student payment")
    pass


def open_notice_board():
    print("open notice board")
    pass


window = Tk()

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
    244.0,
    38.0,
    anchor="nw",
    text="Admin - Home Screen",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("background_image.png"))
image_1 = canvas.create_image(
    155.0,
    235.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("background_image.png"))
image_2 = canvas.create_image(
    359.0,
    235.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("background_image.png"))
image_3 = canvas.create_image(
    563.0,
    235.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_add.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=add_teacher,
    relief="flat"
)
button_1.place(
    x=91.0,
    y=144.0,
    width=130.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_add.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=add_course,
    relief="flat"
)
button_2.place(
    x=295.0,
    y=144.0,
    width=130.0,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_add.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=add_student,
    relief="flat"
)
button_3.place(
    x=499.0,
    y=144.0,
    width=130.0,
    height=40.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_update.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=update_teacher_data,
    relief="flat"
)
button_4.place(
    x=91.0,
    y=201.0,
    width=130.0,
    height=40.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_update.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=update_course_data,
    relief="flat"
)
button_5.place(
    x=295.0,
    y=201.0,
    width=130.0,
    height=40.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_update.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=update_student_data,
    relief="flat"
)
button_6.place(
    x=499.0,
    y=201.0,
    width=130.0,
    height=40.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_remove.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=remove_teacher,
    relief="flat"
)
button_7.place(
    x=91.0,
    y=258.0,
    width=130.0,
    height=40.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_remove.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=remove_course,
    relief="flat"
)
button_8.place(
    x=295.0,
    y=258.0,
    width=130.0,
    height=40.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_remove.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=remove_student,
    relief="flat"
)
button_9.place(
    x=499.0,
    y=258.0,
    width=130.0,
    height=40.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_show_all.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=show_all_teacher,
    relief="flat"
)
button_10.place(
    x=91.0,
    y=315.0,
    width=130.0,
    height=40.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_show_all.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=show_all_course,
    relief="flat"
)
button_11.place(
    x=295.0,
    y=315.0,
    width=130.0,
    height=40.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_show_all.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=show_all_student,
    relief="flat"
)
button_12.place(
    x=499.0,
    y=315.0,
    width=130.0,
    height=40.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_student_payment.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=open_student_payment,
    relief="flat"
)
button_13.place(
    x=174.0,
    y=387.0,
    width=151.0,
    height=40.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_notice_board.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=open_notice_board,
    relief="flat"
)
button_14.place(
    x=384.0,
    y=388.0,
    width=151.0,
    height=40.0
)

canvas.create_text(
    126.0,
    112.0,
    anchor="nw",
    text="Teachers",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    333.0,
    112.0,
    anchor="nw",
    text="Courses",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

canvas.create_text(
    535.0,
    112.0,
    anchor="nw",
    text="Students",
    fill="#000000",
    font=("Roboto", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
