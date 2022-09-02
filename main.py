from tkinter import *
from pick_file import PickFile
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
pick_obj = PickFile()
count = 0
non_guessed = {}
french_list = [key for key, value in pick_obj.lang_dict.items()]

print(len(pick_obj.lang_dict))

window = Tk()
window.minsize(900, 800)
window.config(bg=BACKGROUND_COLOR, pady=20, padx=20)
window.title("Flash Card App")

canvas = Canvas(width=900, height=580, highlightthickness=0, bg=BACKGROUND_COLOR)
image = canvas.create_image(450, 300)
white_img = PhotoImage(file="card_front.png")
green_img = PhotoImage(file="card_back.png")
heading_text = canvas.create_text(440, 200, font=("courier", 40, "italic"))
front_text = canvas.create_text(440, 350, font=("courier", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


def start_game():
    canvas_white()


def right_button_action():
    global count
    key = french_list[count]
    del pick_obj.lang_dict[key]
    del french_list[count]
    window.after(1000, canvas_white)


def wrong_button_action():
    global count
    key = french_list[count]
    value = pick_obj.lang_dict[key]
    non_guessed[key] = non_guessed.setdefault(key, "") + value
    del pick_obj.lang_dict[key]
    del french_list[count]
    window.after(1000, canvas_white())


right_img = PhotoImage(file="right.png")
right_button = Button(width=100, height=100, bg=BACKGROUND_COLOR,
                      highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=right_button_action, image=right_img)
right_button.grid(column=0, row=1)

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(width=100, height=100, bg=BACKGROUND_COLOR,
                      highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=wrong_button_action, image=wrong_img)
wrong_button.grid(column=1, row=1)


def canvas_white():
    global count
    if len(pick_obj.lang_dict):
        count = randint(0, len(pick_obj.lang_dict) - 1)
        key = french_list[count]
        canvas.itemconfig(image, image=white_img)
        canvas.itemconfig(heading_text, text="French", fill="black")
        canvas.itemconfig(front_text, text=key, fill="black")
        window.after(3000, canvas_green)
    else:
        pick_obj.create_non_guessed_file(non_guessed)


def canvas_green():
    global count
    key = french_list[count]
    value = pick_obj.lang_dict[key]
    canvas.itemconfig(image, image=green_img)
    canvas.itemconfig(heading_text, text="English", fill="white")
    canvas.itemconfig(front_text, text=value, fill="white")


start_game()

window.mainloop()

pick_obj.create_non_guessed_file(non_guessed)
