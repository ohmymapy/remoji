import tkinter as tk
names = []
reviews = []
window = tk.Tk()
window.title("Remoji v1.0")

def mainUI():
    global greeting
    global window
    global entry
    global Save

    greeting = tk.Label(text="Welcome to Remoji!\nThe best way to express your comments. ☜(⌒▽⌒)☞\n" "\nWhat is the name of the place?",
    foreground="black", 
    background="gainsboro"
    )
    entry = tk.Entry(fg="black", bg="silver", width=50)
    Save = tk.Button(text = "Done", command= getInput)
    greeting.pack()
    entry.pack()
    Save.pack()
    window.mainloop()
def excellent():
    reviews.append("Excellent")
    close()
def nice():
    reviews.append("Nice")
    close()
def good():
    reviews.append("Good")
    close()
def neutral():
    reviews.append("Neutral")
    close()
def notgood():
    reviews.append("Not So Good")
    close()
def bad():
    reviews.append("Pretty Bad")
    close()

def close():
    global Ending
    global Close
    global others
    global Again
    emotion.destroy()
    Excellent.destroy()
    Nice.destroy()
    Good.destroy()
    Neutral.destroy()
    Notgood.destroy()
    Bad.destroy()
    Ending = tk.Label(text= "Thank you for your review!! (｡◕‿‿◕｡)")
    Close = tk.Button(text= "Close", command= exit)
    others = tk.Button(text= "See other reviews")
    Again = tk.Button(text= "Write another review", command= again)
    Ending.pack()
    Again.pack()
    Close.pack()
    others.pack()

def again():
    Ending.destroy()
    Close.destroy()
    others.destroy()
    Again.destroy()
    mainUI()

def getInput():
    global emotion
    global Excellent
    global Nice
    global Good
    global Neutral
    global Notgood
    global Bad
    name = entry.get()
    names.append(name)
    greeting.destroy()
    entry.destroy()
    Save.destroy()
    emotion = tk.Label(text= "How do you feel after walking out of the door?")
    Excellent = tk.Button(text= "(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧", command= excellent)
    Nice = tk.Button(text= "<(^_^)>", command= nice)
    Good = tk.Button(text= "☉ ‿ ⚆", command= good)
    Neutral = tk.Button(text= "( 0 _ 0 )", command= neutral)
    Notgood = tk.Button(text= "ಠ_ಠ", command= notgood)
    Bad = tk.Button(text= "ಥ﹏ಥ", command= bad)

    emotion.pack()
    Excellent.pack()
    Nice.pack()
    Good.pack()
    Neutral.pack()
    Notgood.pack()
    Bad.pack()

mainUI()