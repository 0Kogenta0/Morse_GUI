from tkinter import *
import RPi.GPIO as GPIO
import time

convert = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-",",":"--..--",":":"---...","?":"..--..","'":".----.","-":"-....-","/":"-..-.","(":"-.--.-",")":"-.--.-","\"":".-..-.","@":".--.-.","=":"-...-","[":"-.--.-","]":"-.--.-","$":"...-..-","+":".-.-.",";":"-.-.-.","_":"..--.-","!":"---."}

led = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

def dot():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.25)

def dash():
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.75)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.25)

def space():
    time.sleep(1.0)

def click():
    text = textentry.get().lower()

    for letter in text:
        if letter == " ":
            space()
        elif letter in convert:
            morseconvert = convert[letter]
            for symbol in morseconvert:
                if symbol == ".":
                    dot()
                elif symbol =="-":
                    dash()
                else:
                    print("Not a '-' or '.'")
            space()
        else:
            print("Character not supported")

def close():
    GPIO.cleanup()
    window.destroy()
    exit()

window = Tk()

lable = Label(window, text="Enter your name:")
lable.grid(row=0, column=0)
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0)
button = Button(window, text="SUBMIT", command=click)
button.grid(row=4, column=0)

exitButton = Button(window, text = 'EXIT', command = close)
exitButton.grid(row=5,column=0)

window.mainloop()