#!/usr/bin/python


from winsound import Beep
from time import sleep
import sys

# set up timing
dur_dot = 100;              # duration of dot (1 unit)
dur_dash = 3 * dur_dot;     # duration of dash (3 units)
delay_intra = dur_dot;      # time between parts of a letter (1 unit)
delay_letter = 3 * dur_dot; # time between letters of a word (3 units)
delay_word = dur_dot;       # time between words (7 units) (but will be surrounded by 2 letter delays)
morse_freq = 1000;           # frequency for dit and dah

# set up global string variables
morse_msg = "";             # string to hold Morse Code message
text_msg = "";              # string to hold ASCII text message

# set up dictionaries:
morse_dict = {
    "A":".-",     "B":"-...",    "C":"-.-.",
    "D":"-..",    "E":".",       "F":"..-.",
    "G":"--.",    "H":"....",    "I":"..",
    "J":".---",   "K":"-.-",     "L":".-..",
    "M":"--",     "N":"-.",      "O":"---",
    "P":".--.",   "Q":"--.-",    "R":".-.",
    "S":"...",    "T":"-",       "U":"..-",
    "V":"...-",   "W":".--",     "X":"-..-",
    "Y":"-.--",   "Z":"--..",
    
    "1":".----",  "2":"..---",
    "3":"...--",  "4":"....-",
    "5":".....",  "6":"-....",
    "7":"--...",  "8":"---..",
    "9":"----.",  "0":"-----",
    
    " ":"|", "\n":"|"
    }

ditdah_dict = {
    ".":dur_dot,
    "-":dur_dash
    };
delay_dict = {
    " ":delay_letter,
    morse_dict[" "]:delay_word
    }

# Make sounds using winsound.Beep(freq,dur);

def txt_2_morse(text_msg):
    my_morse="";
    for ch in text_msg:
        if ch.capitalize() in morse_dict:
            my_morse += morse_dict[ch.capitalize()] + " ";
    return(my_morse);

def play_morse(morse_msg):
    for dd in morse_msg:
        if dd in ditdah_dict: Beep(morse_freq,ditdah_dict[dd]);
        elif dd in delay_dict: sleep(delay_dict[dd]/1000);

def main():
    morse_msg = "";
    if len(sys.argv) > 1: text_msg = sys.argv[1]
    else: text_msg = input("Enter your message to translate: ");
    print(text_msg);
    morse_msg = txt_2_morse(text_msg);

    print(morse_msg);
    
    play_morse(" ");    #pause before playing string.
    play_morse(morse_msg);

    
if __name__ == "__main__":
    main()

   
