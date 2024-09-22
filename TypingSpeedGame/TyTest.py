

#This is for the sample that all the changes in project is done here!


# GUi creating using python
#------------------------------------ Function section --------------------------------------------
from pydoc import text

words = ['A bird in the hand is worth two in the bush.','Caught between a rock and a hard place.','Do I look like a turnip that just fell off the turnip truck?'
         ,'The grass is always greener on the other side.','Just staying one day ahead of yesterday.','A weed is no more than a flower in disguise.','A weed is no more than a flower in disguise.',
         "You can't teach an old dog new tricks.","We'll cross that bridge when we come to it."]

def wordSlider():
    global count,sliderWords
    text = 'How fast can you type?'
    if(count >= len(text)):
        count =0
        sliderWords = ""
    sliderWords += text[count]
    count +=1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(100,wordSlider) #run the label after 50 millisecond

def time():
    global timer,score,miss
    if(timer>=11):
        pass
    else:
        timeCountLabel.configure(fg="red")
    if(timer>0):
        timer -=1
        timeCountLabel.configure(text=timer)
        timeCountLabel.after(1000,time)
    else:
        dataLabel.configure(text="Hit = {} | Miss = {} | Total Score = {}".format(score,miss,score-miss))
        msg = messagebox.askretrycancel("notification","Ooops!...Time up")
        if(msg ==True):
            score = 0
            timer = 60
            miss = 0
            timeCountLabel.configure(text=timer)
            wordLabel.configure(text=words[0])
            scoreCountLabel.configure(text=score)
            missCountLabel.configure(text=miss)
def startGame(event):
    global score,miss
    if(timer == 60):
      time()

    dataLabel.configure(text="")
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreCountLabel.configure(text=score)
        print("Score is ",score)

    else:
        miss +=1
        missCountLabel.configure(text=miss)
        print("missing is",miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])

    #bind the enter button
    wordEntry.delete(0,END)



from tkinter import *
import random
from tkinter import  messagebox



#------------------------------------------ GUI Root Method -------------------------------------------
root = Tk()
root.geometry('860x650+250+150') # size of the box
root.configure(bg='#ff8c00') # background colour
root.title("Typing speed game")
root.iconbitmap('typeGame.ico') # changing the icon or logo on the top left corner
# NOTE : ONLY .ico file can change here
# creating frame


#------------------------------------------- Variable Section --------------------------------------

score =0
timer =60
count =0
sliderWords = ""
miss = 0

#------------------------------------------- Label Methods -----------------------------------------

# font- (text style,size,bold),bg(background colour),fg(forground means text colour)
# for the sliding words label
nameLabel = Label(root,text="Typing Speed Game",font=('Agency FB',30,'bold'),bg='#ff8c00',fg='black')
nameLabel.place(x=300,y=15)

fontLabel = Label(root,text= "",font=('Agency FB',25,'bold'),bg="#cbd121",fg ='black',borderwidth=5, relief='raised', width=40)
fontLabel.place(x=180,y=100)
wordSlider()

# For the words which can be display and user can write them
# Using the random we're going to shuffle all the words
random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('Agency FB',15,'bold'), relief='raised', borderwidth=5, bg="#cbd121", fg="black", height=2, width=80)
wordLabel.place(x=160,y=390)


#This is for the display the score
scoreLabel = Label(root,text="score",font=('Agency FB',25,'bold'),bg="#ff8c00",fg="black")
scoreLabel.place(x=620,y=200)
scoreCountLabel = Label(root,text=score,font=('Agency FB',30,'bold'),bg="#cbd121",fg="black" ,relief='raised', borderwidth=5, width=6 ,height=2)
scoreCountLabel.place(x=610,y=250)

missLabel = Label(root,text="Error",font=('Agency FB',25,'bold'),bg="#ff8c00",fg="black")
missLabel.place(x=190,y=200)
# there is some border properties liks a groove,sunken,raised,flat,solid,ridge
missCountLabel = Label(root,text=miss, font=('Agency FB',30,'bold'),bg="#cbd121",fg="black", relief='raised', borderwidth=5, width=6, height=2)
missCountLabel.place(x =170,y =250)


# This is for the display the time
timeLabel = Label(root, text="Time", font=('Agency FB', 25, 'bold'), bg="#ff8c00", fg="black")
timeLabel.place(x=410, y=200)
timeCountLabel = Label(root, text=timer, font=('Agency FB', 30, 'bold'), bg="#cbd121", fg="blue", relief='raised', borderwidth=5, width=6, height=2)
timeCountLabel.place(x=390, y=250)


# This is for the details of the plalying this game
dataLabel = Label(root,text="Type words and Enter the button",font=('Agency FB', 25, 'bold'),bg="#ff8c00", fg="black")
dataLabel.place(x=250,y=550)
# #---------------------------------------------- Input method from user -----------------------------------

# bd = border
wordEntry = Entry(root, font=('Agency FB', 25, 'bold'), borderwidth=5, relief='raised', bg='oldlace', justify="center", width=25)  #justify for the center text
wordEntry.focus_set()
wordEntry.place(x=250, y=480)

#-------------------------------------------------###-----------------------------------------------------------

root.bind('<Return>', startGame)  # this return tense to the Enter button

root.mainloop()