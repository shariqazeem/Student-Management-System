from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, StringVar

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def checkUsernameAndPassword(username_string, password_string):
    if username_string == "student123" and password_string == "password@123":
        return True
    else:
        return False


def login_button_click():
    if username.get() == "":
        messagebox.showerror("Error", "Username is empty!")
    elif password.get() == "":
        messagebox.showerror("Error", "Password is empty!")
    elif not checkUsernameAndPassword(username.get(), password.get()):
        messagebox.showerror("Error", "Username & Password is Incorrect!")
    else:
        window.destroy()
        import student_home_screen
        obj = student_home_screen


window = Tk()

# variable
username = StringVar()
password = StringVar()

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
    228.0,
    59.0,
    anchor="nw",
    text="Student Login",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    147.0,
    128.0,
    anchor="nw",
    text="Username  ",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("textbox_rounded_corner.png"))
entry_bg_1 = canvas.create_image(
    354.0,
    136.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    textvariable=username
)
entry_1.place(
    x=269.0,
    y=122.0,
    width=170.0,
    height=26.0
)

canvas.create_text(
    147.0,
    174.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Roboto", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("textbox_rounded_corner.png"))
entry_bg_2 = canvas.create_image(
    354.0,
    182.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E9E8E8",
    highlightthickness=0,
    show="*",
    textvariable=password
)
entry_2.place(
    x=269.0,
    y=168.0,
    width=170.0,
    height=26.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_student_round_corner.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login_button_click,
    relief="flat"
)
button_1.place(
    x=242.0,
    y=256.0,
    width=96.0,
    height=41.0
)

window.resizable(False, False)
window.mainloop()
