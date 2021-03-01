from tkinter import Tk, Label, Button, PhotoImage, ttk, StringVar
import random
from time import sleep

tired = random.randrange(10,98, 1)

class EyeTrackerGUI:
    def __init__(self, master):
        self.master = master
        master.title("ICare")

        self.label = Label(master, text="Take your first step towards wellbeing")
        self.label.pack()

        self.greet_button = Button(master, text="Check", command=self.greet)
        self.greet_button.pack()

        self.tired_button = Button(master, text="Am I Tired?", command=self.tired)
        self.tired_button.pack()

        display_text = StringVar()
        self.display = Label(master, textvariable=display_text)
        self.display.pack()


        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        sleep(3)
        print("Analyzing Face...")
        sleep(3)
        print("Extracting Data...")
        sleep(3)
        print("Compiling Results...")
        sleep(2)
        print("Complete")

    

    def tired(self):
        print("Your tiredness is " + str(tired) + "%")
        if tired < 20:
            print("You are doing great!!")
        elif tired >= 21 and tired <= 40:
            print("You are getting tired, take some deep breaths for 10 seconds")
            sleep(10)
            print("You are doing great, keep working now")
        elif tired >= 41 and tired <= 70:
            print("Stretch for 1 minute!!!")
            sleep(60)
            print("Great, now keep woking")
        else:
            print("Take a 10 minute break")
            sleep(600)
            print("Keep Working")

root = Tk()
my_gui = EyeTrackerGUI(root)
root.mainloop()

