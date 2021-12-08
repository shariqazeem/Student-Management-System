from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def admin_button_click():
    window.destroy()
    import admin_login_screen
    obj = admin_login_screen


def teacher_button_click():
    window.destroy()
    import teacher_login_screen
    obj = teacher_login_screen


def student_button_click():
    window.destroy()
    import student_login_screen
    obj = student_login_screen


window = Tk()

window.geometry("591x344")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=344,
    width=591,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    138.0,
    89.0,
    anchor="nw",
    text="Student Management System",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_admin_round_corner.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=admin_button_click,
    relief="flat"
)
button_1.place(
    x=100.0,
    y=170.0,
    width=96.0,
    height=41.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_teacher_round_corner.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=teacher_button_click,
    relief="flat"
)
button_2.place(
    x=248.0,
    y=170.0,
    width=96.0,
    height=41.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_student_round_corner.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=student_button_click,
    relief="flat"
)
button_3.place(
    x=396.0,
    y=170.0,
    width=96.0,
    height=41.0
)
window.resizable(False, False)
window.mainloop()
