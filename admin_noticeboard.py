import datetime
from pathlib import Path
import mysql.connector  # pip install mysql-connector-python
from tkinter import Tk, Canvas, Button, PhotoImage, messagebox, END, StringVar, Frame, ttk, HORIZONTAL, VERTICAL, X, Y, \
    BOTTOM, RIGHT, BOTH

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


def add_notice():
    date_object = datetime.date.today()
    print(date_object)


def fetch_data():
    connection = mysql.connector.connect(host=db_host,
                                         username=db_username,
                                         password=db_password,
                                         database=db_database)
    cursor = connection.cursor()
    cursor.execute("select * from notice_board")
    data = cursor.fetchall()
    if len(data) != 0:
        noticeboard_table.delete(*noticeboard_table.get_children())
        for i in data:
            noticeboard_table.insert("", END, values=i)
        connection.commit()
    connection.close()


def get_cursor(event=""):
    cursor_row = noticeboard_table.focus()
    content = noticeboard_table.item(cursor_row)
    data = content["values"]

    notice_id.set(data[0])
    notice_body.set(data[1])
    notice_submitted_by.set(data[2])
    notice_date.set(data[2])


def onDoubleClick(event=""):
    cursor_row = noticeboard_table.focus()
    content = noticeboard_table.item(cursor_row)
    data = content["values"]
    messagebox.showinfo("Success", data[1], parent=window)


window = Tk()

notice_id = StringVar()
notice_body = StringVar()
notice_submitted_by = StringVar()
notice_date = StringVar()

db_host = all_credentials.host
db_username = all_credentials.username
db_password = all_credentials.password
db_database = all_credentials.database
db_noticeboard = all_credentials.noticeboard_table_name

window.geometry("960x533")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=533,
    width=960,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    411.0,
    28.0,
    anchor="nw",
    text="Notice Board",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    383.0,
    67.0,
    anchor="nw",
    text="Below are all notice in the table",
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
    width=58.0,
    height=32.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_admin_show_all_teacher.png"))
image_1 = canvas.create_image(
    477.0,
    279.0,
    image=image_image_1
)

# Notice Table & scroll bar
table_frame = Frame(window, bd=4, relief="ridge")
table_frame.place(x=51, y=112, width=852, height=335)

scroll_bar_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
scroll_bar_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
noticeboard_table = ttk.Treeview(table_frame, column=("notice_id",
                                                      "notice_body",
                                                      "notice_submitted_by",
                                                      "notice_date"),
                                 xscrollcommand=scroll_bar_x.set,
                                 yscrollcommand=scroll_bar_y.set)
scroll_bar_x.pack(side=BOTTOM, fill=X)
scroll_bar_y.pack(side=RIGHT, fill=Y)

scroll_bar_x.config(command=noticeboard_table.xview)
scroll_bar_y.config(command=noticeboard_table.yview)

noticeboard_table.heading("notice_id", text="Notice ID")
noticeboard_table.heading("notice_body", text="Notice Body")
noticeboard_table.heading("notice_submitted_by", text="Notice Submitted by")
noticeboard_table.heading("notice_date", text="Notice Date")

noticeboard_table["show"] = "headings"

noticeboard_table.column("notice_id", width=70)
noticeboard_table.column("notice_body", width=250)
noticeboard_table.column("notice_submitted_by", width=70)
noticeboard_table.column("notice_date", width=50)

ttk.Style().configure('Treeview', rowheight=30)

noticeboard_table.pack(fill=BOTH, expand=1)
noticeboard_table.bind("<ButtonRelease>", get_cursor)
noticeboard_table.bind("<Double-1>", onDoubleClick)
fetch_data()

button_image_2 = PhotoImage(
    file=relative_to_assets("button_admin_add_notice.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=add_notice,
    relief="flat"
)
button_2.place(
    x=169.0,
    y=465.0,
    width=117.0,
    height=41.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_admin_update_notice.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=409.0,
    y=465.0,
    width=117.0,
    height=41.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_admin_delete_notice.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=669.0,
    y=465.0,
    width=117.0,
    height=41.0
)
window.resizable(False, False)
window.mainloop()
