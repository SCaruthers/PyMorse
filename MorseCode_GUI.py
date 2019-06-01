#!/usr/bin/python

import MorseCode
from tkinter import *


root = Tk()
root.title("Morse Code Translator")
 
# Code to add widgets will go here...

my_msg = StringVar()
label_msg = StringVar()

def BtCallBack():
    my_msg.set(MorseCode.txt_2_morse(text_msg.get(1.0,"end-1c")))
    #my_msg.set(MorseCode.txt_2_morse("Hi"))
    #print(text_msg.get(1.0,END))
    
def BpCallBack():
    MorseCode.play_morse(" ")
    MorseCode.play_morse(my_msg.get())

def BcCallBack():
    text_msg.delete(1.0, END)
    BtCallBack()

def BqCallBack():
    root.destroy()
    quit()

text_lbl = Label( root, textvariable=label_msg, anchor = W )
label_msg.set("Message to be encoded")

text_msg = Text( root, height = 3 )

text_msg.insert(INSERT, "Type your message to be translated here")


Bt = Button(root, text ='Translate', width = 20, command = BtCallBack)
Bc = Button(root, text ='Clear Message', width = 20, command = BcCallBack)
Bq = Button(root, text = 'Quit', width = 20, command = BqCallBack)

morse_label = Message( root, width = 500, textvariable=my_msg, font=("Times", "11") )
my_msg.set("Morse code will show here")

Bp = Button (root, text = 'Play',width = 20, command = BpCallBack)

text_lbl.grid( row = 0, column = 0 )
text_msg.grid( row = 1, column = 0, rowspan = 2, columnspan = 3)
Bc.grid(row = 3, column = 0)
Bt.grid(row = 3, column = 1)
Bq.grid(row =3, column = 2)
morse_label.grid( row = 4, column = 0, rowspan = 2, columnspan = 3)
Bp.grid( row = 6, column = 1)



root.mainloop()
