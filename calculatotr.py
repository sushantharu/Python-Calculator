import tkinter as tk

# Main window create garne
root = tk.Tk()

# Window ko title
root.title("My Calculator")

# Window ko size
root.geometry("350x500")

# Window resize disable garne
root.resizable(False, False)

# Background color
root.configure(bg="#222222")


# =========================
# DISPLAY
# =========================

display = tk.Entry(
    root,
    font=("Arial", 28),
    justify="right",
    bg="#f5f5f5",
    fg="black",
    bd=10
)

# Display lai screen ma rakhne
display.pack(
    padx=20,
    pady=20,
    fill="x",
    ipady=15
)


# =========================
# FUNCTIONS
# =========================

def add_to_display(value):
    # Number/operator display ma add garne
    display.insert(tk.END, value)


def clear_display():
    # Pura display clear garne
    display.delete(0, tk.END)


def delete_last():
    # Display ko current value line
    current = display.get()

    # Display clear garne
    display.delete(0, tk.END)

    # Last character hataera feri display ma rakhne
    display.insert(0, current[:-1])


def calculate():
    # Calculation garna try block use garne
    try:

        # Display bata expression line
        expression = display.get()

        # Expression calculate garne
        result = eval(expression)

        # Display clear garne
        display.delete(0, tk.END)

        # Result display ma dekhाउने
        display.insert(0, result)

    except:

        # Error aayo bhane display clear garne
        display.delete(0, tk.END)

        # Error message dekhाउने
        display.insert(0, "Error")


def percentage():
    # Percentage calculate garne
    try:

        # Display ko value lai float ma convert garne
        value = float(display.get())

        # Percentage calculate garne
        result = value / 100

        # Display clear garne
        display.delete(0, tk.END)

        # Result display ma rakhne
        display.insert(0, result)

    except:

        # Error aayo bhane display clear garne
        display.delete(0, tk.END)

        # Error dekhाउने
        display.insert(0, "Error")


# =========================
# BUTTON FRAME
# =========================

button_frame = tk.Frame(
    root,
    bg="#C726C7"
)

# Frame lai screen ma rakhne
button_frame.pack(
    padx=15,
    pady=5,
    fill="both",
    expand=True
)


# =========================
# BUTTON FUNCTION
# =========================

def create_button(text, row, column, command):
    # Button create garne function

    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18, "bold"),
        command=command,
        bg="#5CB32D",
        fg="white",
        activebackground="#551DB5",
        bd=0
    )

    # Button lai grid ma rakhne
    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5,
        sticky="nsew"
    )


# =========================
# BUTTONS
# =========================

create_button("C", 0, 0, clear_display)
# Clear button

create_button("DEL", 0, 1, delete_last)
# Delete button

create_button("%", 0, 2, percentage)
# Percentage button

create_button("/", 0, 3, lambda: add_to_display("/"))
# Divide button


create_button("7", 1, 0, lambda: add_to_display("7"))
# Number 7

create_button("8", 1, 1, lambda: add_to_display("8"))
# Number 8

create_button("9", 1, 2, lambda: add_to_display("9"))
# Number 9

create_button("*", 1, 3, lambda: add_to_display("*"))
# Multiply button


create_button("4", 2, 0, lambda: add_to_display("4"))
# Number 4

create_button("5", 2, 1, lambda: add_to_display("5"))
# Number 5

create_button("6", 2, 2, lambda: add_to_display("6"))
# Number 6

create_button("-", 2, 3, lambda: add_to_display("-"))
# Minus button


create_button("1", 3, 0, lambda: add_to_display("1"))
# Number 1

create_button("2", 3, 1, lambda: add_to_display("2"))
# Number 2

create_button("3", 3, 2, lambda: add_to_display("3"))
# Number 3

create_button("+", 3, 3, lambda: add_to_display("+"))
# Plus button


create_button("0", 4, 0, lambda: add_to_display("0"))
# Number 0

create_button(".", 4, 1, lambda: add_to_display("."))
# Decimal point

create_button("=", 4, 2, calculate)
# Equal button


# =========================
# GRID SETTINGS
# =========================

for row in range(5):
    # 5 ota row ko size equal banaune
    button_frame.rowconfigure(row, weight=1)


for column in range(4):
    # 4 ota column ko size equal banaune
    button_frame.columnconfigure(column, weight=1)


# =========================
# PROGRAM START
# =========================

root.mainloop()
# Calculator window start garne




#  frontend ko lagi maile Tkinter use gareko chu. Tkinter Python ko GUI library ho,
#  jasle window, button, input box jasta graphical components banauna help garcha.
#  GUI ko full form Graphical User Interface ho.
#  GUI bhaneko user le screen ma dekhe ra mouse/keyboard bata use garne graphical interface ho.