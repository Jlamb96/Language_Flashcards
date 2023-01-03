from tkinter import *
import pandas
import random
import sys
import os
from tkinter import messagebox
GERMAN = "data/geman_words.csv"
FRENCH = "data/french_words.csv"
PORTUGUESE = "data/portuguese_words.csv"
SPANISH = "data/spanish_words.csv"
LANGUAGE = None
French_string = "French"
German_string = "German"
Portuguese_string = "Portuguese"
Spanish_string = "Spanish"
Chosen_language = None
BACKGROUND_COLOR = "#B1DDC6"
eng_word = ""
card_choice = None
language_not_picked = True
language_window = None

def pick_word():
    global eng_word, card_choice
    try:
        german = pandas.read_csv(f"{Chosen_language}words_to_learn.csv")
    except FileNotFoundError:
        german = pandas.read_csv(LANGUAGE)
    finally:
        canvas.itemconfig(front_image, image=front)
        count = len(german[Chosen_language])
        card_choice = random.randint(0, count)
        ger_word = (german[Chosen_language][card_choice])
        eng_word = (german[" English"][card_choice])
        language.config(text=Chosen_language, bg="white", fg="black")
        word.config(text=ger_word, bg="white", fg="black")
        if len(ger_word) > 6:
            word.place(x=265, y=200)
        else:
            word.place(x=290, y=200)
        count_down(4)


def count_down(seconds):
    if seconds != 0:
        window.after(1000, count_down, seconds - 1)
    else:
        show_english()


def show_english():
    global eng_word, word
    canvas.itemconfig(front_image, image=back)
    language.config(text="English", font=("Ariel", 40, "italic"), bg="#91c2af", fg="white")
    language.place(x=290, y=100)
    word.config(text=eng_word, bg="#91c2af", fg="white")


def x_button_press():
    pick_word()

def french():
    global Chosen_language, LANGUAGE, language_not_picked
    Chosen_language = French_string
    LANGUAGE = FRENCH
    language_not_picked = False
    language_window.destroy()

def german():
    global Chosen_language, LANGUAGE, language_not_picked
    Chosen_language = German_string
    LANGUAGE = GERMAN
    language_not_picked = False
    language_window.destroy()

def portuguese():
    global Chosen_language, LANGUAGE, language_not_picked
    Chosen_language = Portuguese_string
    LANGUAGE = PORTUGUESE
    language_not_picked = False
    language_window.destroy()

def spanish():
    global Chosen_language, LANGUAGE, language_not_picked
    Chosen_language = Spanish_string
    LANGUAGE = SPANISH
    language_not_picked = False
    language_window.destroy()

def reset_progress():
    global language_not_picked
    answer = messagebox.askyesno(title="Are you sure?", message=f"Are you sure you want to clear all your learned progress in {Chosen_language}?")
    if answer:
        if os.path.exists(f"{Chosen_language}words_to_learn.csv"):
            os.remove(f"{Chosen_language}words_to_learn.csv")
            messagebox.showinfo(message=f"Progress in {Chosen_language} deleted. ")
            window.destroy()
            language_not_picked = True
            start()
        else:
            messagebox.showinfo(message="You do not have progress to delete yet.")

def check_button():
    try:
        german = pandas.read_csv(f"{Chosen_language}words_to_learn.csv")
    except FileNotFoundError:
            german = pandas.read_csv(LANGUAGE)
    finally:
        german.drop([card_choice], axis=0, inplace=True)
        german.to_csv(f"{Chosen_language}words_to_learn.csv", index=False, encoding="utf-8-sig")
        pick_word()

def go_back():
    global language_not_picked
    window.destroy()
    language_not_picked = True
    start()

def exit():
    sys.exit()

def start():
    global language_window
    while language_not_picked:
        language_window = Tk()
        language_window.title("Pick a language to learn")
        language_window.config(bg=BACKGROUND_COLOR, padx=100,pady=100)
        german_flag = PhotoImage(file="images/German_flag.png")
        french_flag = PhotoImage(file="images/French_flag.png")
        portuguese_flag = PhotoImage(file="images/Brasil.png")
        exit_button_img = PhotoImage(file="images/exit.png")
        spanish_flag = PhotoImage(file="images/spanish_flag.png")

        german_label = Label(text="German", font=("Ariel", 40, "italic"), bg=BACKGROUND_COLOR, fg="white")
        german_label.grid(column=0, row=0)
        German_button = Button(image=german_flag, command=german, highlightthickness=0)
        German_button.grid(column=0, row=1, padx=50, pady=50)

        French_button = Button(image=french_flag, command=french, highlightthickness=0)
        French_button.grid(column=1, row=1, padx=50, pady=50)
        french_label = Label(text="French", font=("Ariel", 40, "italic"), bg=BACKGROUND_COLOR, fg="white")
        french_label.grid(column=1, row=0)

        portuguese_button = Button(image=portuguese_flag, command=portuguese, highlightthickness=0)
        portuguese_button.grid(column=3, row=1, padx=50, pady=50)
        portuguese_label = Label(text="Portuguese", font=("Ariel", 40, "italic"), bg=BACKGROUND_COLOR, fg="white")
        portuguese_label.grid(column=3, row=0)

        spanish_button = Button(image=spanish_flag, command=spanish, highlightthickness=0)
        spanish_label = Label(text="Spanish", font=("Ariel", 40, "italic"), bg=BACKGROUND_COLOR, fg="white")
        spanish_label.grid(column=4, row=0)
        spanish_button.grid(column=4, row=1)

        exit_button = Button(image=exit_button_img, command=exit)
        exit_button.grid(column=2, row=2)
        language_window.mainloop()

while True:
    start()
    window = Tk()
    window.title("Language Flashcards")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    canvas = Canvas(height=526, width=800, highlightthickness=0)
    canvas.config(bg=BACKGROUND_COLOR)
    front = PhotoImage(file="images/card_front.png")
    back = PhotoImage(file="images/card_back.png")
    front_image = canvas.create_image(400, 260, image=front)
    canvas.grid(column=1, row=1, columnspan=2, rowspan=1)
    language = Label(text="", font=("Ariel", 40, "italic"))
    language.place(x=290, y=100)
    check_mark = PhotoImage(file="images/right.png")
    x_mark = PhotoImage(file="images/wrong.png")
    go_back_img = PhotoImage(file="images/back.png")
    check_button = Button(image=check_mark, command=check_button, highlightthickness=0)
    check_button.grid(column=2, row=2)
    x_button = Button(image=x_mark, command=x_button_press, highlightthickness=0)
    x_button.grid(column=1, row=2)
    word = Label(text="", font=("Ariel", 60, "bold"))
    word.place(x=290, y=100)
    language = Label(text="", font=("Ariel", 40, "italic"))
    language.place(x=290, y=100)
    go_back_button = Button(image=go_back_img, command=go_back, highlightthickness=0, bg=BACKGROUND_COLOR)
    go_back_button.place(x=350,y=526)
    reset_progess_button = Button(text=f"Reset progress on {Chosen_language}", command=reset_progress)
    reset_progess_button.place(x=-40, y=-40)

    pick_word()

    count_down(4)

    window.mainloop()

