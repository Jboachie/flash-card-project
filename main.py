from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
#---------------------------------------------WORDS/CARDS SWITCHING-------------------------------------------------------
try:
    frenchwords = pandas.read_csv("./data/words_to_learn")
except FileNotFoundError:
    original_frenchwords = pandas.read_csv("./data/french_words.csv")
    french_words = original_frenchwords.to_dict("records")
else:
    french_words = frenchwords.to_dict("records")
current_card = {}
def word_switch():
    global current_card
    current_card = random.choice(french_words)
    canvas.itemconfig(lang_word, text=current_card["French"])
    canvas.itemconfig(lang_title, text="French", fill= "black")
    canvas.itemconfig(front, image=fl_front)
    window.after(3000, card_flip)


def card_flip():
    canvas.itemconfig(front, image=fl_back)
    canvas.itemconfig(lang_title, text="English", fill="white")
    canvas.itemconfig(lang_word, text = current_card["English"])

def is_known():
    french_words.remove(current_card)
    data = pandas.DataFrame(french_words)
    data.to_csv("./data/words_to_learn", index= False)
    print(len(french_words))
    word_switch()


#---------------------------------------------SAVING PROGRESS-------------------------------------------------------

#--------------------------------UI----------------------------------------------------
window = Tk()
window.title("Flashcard revision")
window.config(padx=20, pady=20, bg= BACKGROUND_COLOR)


canvas = Canvas(width = 800, height= 576, bg=BACKGROUND_COLOR, highlightthickness=0)
fl_front = PhotoImage(file = "./images/card_front.png")
fl_back = PhotoImage(file = "./images/card_back.png")
right_img = PhotoImage(file = "./images/right.png")
wrong_img = PhotoImage(file = "./images/wrong.png")
front = canvas.create_image(400,262, image = fl_front)
right = Button(image=right_img, highlightthickness=0, command=is_known)
wrong = Button(image=wrong_img, highlightthickness=0, command=word_switch)
canvas.grid(column = 1, row = 1, columnspan = 2)
right.grid(column = 1, row = 2)
wrong.grid(column = 2, row = 2)
lang_title = canvas.create_text(400,150, text = "",fill = "black", font= ("Arial", 40, "italic"))
lang_word = canvas.create_text(400,263, text = "",fill = "black", font= ("Arial", 60, "bold"))

word_switch()


window.mainloop()


