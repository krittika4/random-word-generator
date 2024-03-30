# -*- coding: utf-8 -*-
from tkinter import *
import random

root=Tk()
root.geometry("500x500")
root.title("Random Word Generator")

random_word_generated = Label(root)

def random_word():
    alpha_list = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    print(alpha_list)
    random_no1 = random.randint(1,25)
    random_no2 = random.randint(1,25)
    random_no3 = random.randint(1,25)
    random_no4 = random.randint(1,25)
    random_no5 = random.randint(1,25)
    random_alpha1 = alpha_list[random_no1]
    random_alpha2 = alpha_list[random_no2]
    random_alpha3 = alpha_list[random_no3]
    random_alpha4 = alpha_list[random_no4]
    random_alpha5 = alpha_list[random_no5]
    random_word_generated["text"]=random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5

    

btn = Button(root, text = "Generate Random Word", command = random_word)
btn.place(relx=0.4, rely=0.5, anchor=CENTER)

random_word_generated.place(relx = 0.5, rely = 0.6, anchor = CENTER)


root.mainloop()





