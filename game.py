from tkinter import *
import random
import time
from tkinter import messagebox
import tkinter.scrolledtext as tkscroll
import os 
import os.path
import webbrowser
import json

def setmenuwindowDimensions(w,h):
    ws = window.winfo_screenwidth()                                 #computers screen size
    hs = window.winfo_screenheight()    
    x = (ws/2) - (w/2)                                              #here we are using screen dimensions
    y = (hs/2) - (h/2)                                              #to calculate center points for x and y
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))                   #window size
    return window 

def setgamewindowDimensions(w,h):
    ws = window2.winfo_screenwidth()                                    
    hs = window2.winfo_screenheight()   
    x = (ws/2) - (w/2)                                              
    y = (hs/2) - (h/2)                                              
    window2.geometry('%dx%d+%d+%d' % (w, h, x, y))          
    return window2 

def setpausewindowDimensions(w,h):
    ws = window3.winfo_screenwidth()                                    
    hs = window3.winfo_screenheight()   
    x = (ws/2) - (w/2)                                              
    y = (hs/2) - (h/2)                                              
    window3.geometry('%dx%d+%d+%d' % (w, h, x, y))          
    return window3 

def setleaderboardwindowDimensions(w,h):
    ws = window4.winfo_screenwidth()                                    
    hs = window4.winfo_screenheight()   
    x = (ws/2) - (w/2)                                              
    y = (hs/2) - (h/2)                                              
    window4.geometry('%dx%d+%d+%d' % (w, h, x, y))          
    return window4 

def setbossKeyWindowDimensions(w,h):
    ws = window5.winfo_screenwidth()                                    
    hs = window5.winfo_screenheight()   
    x = (ws/2) - (w/2)                                              
    y = (hs/2) - (h/2)                                              
    window5.geometry('%dx%d+%d+%d' % (w, h, x, y))          
    return window5 

def setConfigureWindowDimensions(w,h):
    ws = window6.winfo_screenwidth()                                    
    hs = window6.winfo_screenheight()   
    x = (ws/2) - (w/2)                                              
    y = (hs/2) - (h/2)                                              
    window6.geometry('%dx%d+%d+%d' % (w, h, x, y))          
    return window6 

def menuwindow():                                                   #setting menu window
    global window, width, height
    window = Tk()                                                   #creating window
    window.title("MENU")                                            #title of the window
    width = 550  #width of snake's world
    height = 550 #height of snake's world
    window = setmenuwindowDimensions(width, height)                 #calling function that will set dimensions of window

def gamewindow():
    global canvas, window2
    window.withdraw()
    window2 = Tk()
    window2.title("SNAKE GAME")                                     
    width = 550  #width of snake's world
    height = 550 #height of snake's world
    window2 = setgamewindowDimensions(width, height)                            
    canvas = Canvas(window2, bg="black", width=width, height=height)

def pausewindow():
    global window3
    window3 = Tk()
    window3.title("SNAKE GAME PAUSED")
    window3.configure(background = "black")                                     
    width = 550  #width of snake's world
    height = 550 #height of snake's world
    window3 = setpausewindowDimensions(width, height)                          

def leaderboardwindow():
    global window4
    window4 = Tk()
    window4.title("LEADERBOARD")
    window4.configure(background = "black")                                     
    width = 550  #width of snake's world
    height = 550 #height of snake's world
    window4 = setleaderboardwindowDimensions(width, height)

def bossKeyWindow():
    global window5
    window5 = Tk()
    window5.title("BOSS KEY")
    window5.configure(background = "black")                                     
    width = 550  #width of snake's world
    height = 550 #height of snake's world
    window5 = setbossKeyWindowDimensions(width, height)

def configureWindow():
    global window6
    window6 = Tk()
    window6.title("CONFIGURE GAME")
    window6.configure(background = "black")                                     
    width = 550  #width of snake's world
    height = 550 #height of snake's world
    window6 = setConfigureWindowDimensions(width, height)

def openWebNDestroyBossMessage():
    webbrowser.open('https://www.cs.manchester.ac.uk/')                 #opening webbrowser to hide game
    window5.destroy()


#works for menu, when paused game, when playing
def bossKey(event):
    bossKeyWindow()
    #bossKeyphoto = PhotoImage(window5, file="sh.png")
    close_label = Label(window5, text="Boss Key: Activated", bg="#000000", foreground="#ffffff",
                            font=("Times New Roman", 35, "bold"))
    close_label.pack()
    window5.after(150, openWebNDestroyBossMessage)

def startGamewhenKeyPressed(event):                                     #when any key is pressed, start the game
    gamefunction()

def switchStart():                                                      #function for making start able after submitting nickname
    global strtButton, submitnickButton, window
    if(strtButton['state']==NORMAL):
        strtButton["state"] = DISABLED
        submitnickButton["text"]="submit"
    elif (strtButton['state']==DISABLED):
        strtButton["state"]=NORMAL
        submitnickButton["text"]="submitted"
        submitnickButton["state"]=DISABLED
        window.bind('<Return>', startGamewhenKeyPressed)                #when submit botton DISABLED then allow press any key affect starting the game

def clickNameBox(event):                                                #function to clear the content of nameBox
    nameBox.configure(state=NORMAL)
    nameBox.delete(0, END)
    nameBox.unbind('<Button-1>', nameBoxClicked)

def EnterNickname():
    global currentPlayer
    switchStart()
    if nameBox.get() == "Enter Your Nickname Here...":
        currentPlayer = "NewPlayer"
    else:
        currentPlayer = nameBox.get()
    helloMessage = "Thanks for playing " + currentPlayer + "." + "\n" + "Press <Return> or Click 'start' to play."
    label = Label(window, text = helloMessage)
    label.pack()

def nickinput():
    global nameBox, submitnickButton, nameBoxClicked
    nameBox = Entry(window, width = 25, bd= 10)                         #input of user
    nameBox.pack()
    nameBox.insert(0, "Enter Your Nickname Here..." )
    nameBoxClicked = nameBox.bind('<Button-1>', clickNameBox)
    submitnickButton = Button(window, text="Submit", command= EnterNickname, bg="#08fd00", foreground="#ffffff", font=("helvetica", 25))
    submitnickButton.pack()
    label4 =Label(window, text="", bg="#000000", foreground="#000000", font=("Times New Roman", 20, "bold"))
    label4.pack()

def exitbutton():
    global quitButton
    if quitButton:
        if messagebox.askokcancel("Exit", "Wanna leave?"):
            window.quit()
        quitButton = False
    if not quitButton:
        quitButton = True

def menu():
    global quitButton, strtButton
    menuwindow()
    window.configure(background = "black")
    label1 =Label(window, text="Snake Game", bg="#05670c", foreground="#ffffff", font=("Times New Roman", 35, "bold"))
    label1.pack()
    label2 =Label(window, text="", bg="#000000", foreground="#000000", font=("Times New Roman", 10, "bold"))
    label2.pack()
    strtButton = Button(window, text="start",bg="#08fd00",command= gamefunction, foreground="#ffffff", font=("helvetica", 25), state=DISABLED)
    strtButton.pack()
    loadButton = Button(window, text="load",bg="#08fd00", command=loadGame, foreground="#ffffff", font=("helvetica", 25))  #assign command, load should go directly to pause window, because you saved it there
    loadButton.pack()
    leaderButton = Button(window, text="leaderboard",command = leaderboard, bg="#08fd00", foreground="#ffffff", font=("helvetica", 27))
    leaderButton.pack()
    configureButton = Button(window, text="configure",command= configure, bg="#08fd00", foreground="#ffffff", font=("helvetica", 27))
    configureButton.pack()
    label3 =Label(window, text="", bg="#000000", foreground="#000000", font=("Times New Roman", 20, "bold"))
    label3.pack()
    nickinput()
    quitButton = False
    quitButton = Button(window, text = "EXIT GAME", command = exitbutton, bg="#fd6600", foreground="#ffffff", font=("helvetica", 24))
    quitButton.pack()
    window.bind('<Escape>', bossKey)

def growSnake():
    global scoreText, txt, score
    lastElement = len(snake)-1                                          #we must subtract 1 because lists start with an index of 0
    lastElementPos = canvas.coords(snake[lastElement])
    snake.append(canvas.create_oval(0,0, snakeSize,snakeSize,           #creating and appending a new oval to the snake data structure. 
        fill="#FDF3F3"))
    if (direction == "left"):                                           #if the snake is moving left, we move the element that we just created to the right of the last element
        canvas.coords(snake[lastElement+1],
            lastElementPos[0]+snakeSize,
            lastElementPos[1],
            lastElementPos[2]+snakeSize,lastElementPos[3])          
    elif (direction == "right"):                                        #snake direction is right, we place the new snake element to the left of the last element
        canvas.coords(snake[lastElement+1],
            lastElementPos[0] -snakeSize,
            lastElementPos[1],lastElementPos[2] -snakeSize,lastElementPos[3])
    elif (direction == "up"):                                           #snake direction is up, we place the new snake element to the bottom of the last element
        canvas.coords(snake[lastElement+1],
            lastElementPos[0],
            lastElementPos[1]+snakeSize,
            lastElementPos[2],lastElementPos[3]+snakeSize)
    else:                                                               #snake direction is down, we place the new snake element to the top of the last element
        canvas.coords(snake[lastElement+1],
            lastElementPos[0],
            lastElementPos[1]-snakeSize,
            lastElementPos[2],lastElementPos[3]-snakeSize)
    score += 1                                                          #incrementing score...everytime we grow snake
    txt = "Score:" + str(score) + " "
    canvas.itemconfigure(scoreText, text=txt)                           #we update the canvas by calling the itemconfigure function
    window2.bind('<b>', cheatCodeaddPointsToScore)                      #CHEAT CODE

def moveFood():
    global food, foodX, foodY
    canvas.move(food, (foodX*(-1)), (foodY*(-1)))                       #move the food back to its original starting point (0,0) by multiplying the current coordinates by -1
    foodX = random.randint(0,width-snakeSize)
    foodY = random.randint(0,height-snakeSize)  
    canvas.move(food, foodX, foodY)

def moveFood2():
    global food2, foodX2, foodY2                                        #move the food back to its original starting point (0,0) by multiplying the current coordinates by -1
    canvas.move(food2, (foodX2*(-1)), (foodY2*(-1)))
    foodX2 = random.randint(10,width-snakeSize)
    foodY2 = random.randint(10,height-snakeSize)  
    canvas.move(food2, foodX2, foodY2)

def moveFood3():
    global food3, foodX3, foodY3
    canvas.move(food3, (foodX3*(-1)), (foodY3*(-1)))                   
    foodX3 = random.randint(20,width-snakeSize)
    foodY3 = random.randint(20,height-snakeSize)  
    canvas.move(food3, foodX3, foodY3)

def overlapping(a,b):                                                   #collision detection function routine
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:     #determines if the rectangles are overlapping
        return True
    return False

def deleteFromSnakeList(event):
    global snake
    if len(snake) > 1:                                                  #so it leaves the head of snake
        canvas.delete(snake[len(snake)-1])                              #deleting one of snake
        snake.pop()

def cheatCodeaddPointsToScore(event):
    global score, scoreText, txt
    score += 1
    txt = "Score:" + str(score) + " "
    canvas.itemconfigure(scoreText, text=txt)

def cheatCodeMakeSnakeSmaller():
    if score >= 10:
        window2.bind('<v>', deleteFromSnakeList)                        #CHEAT CODE

def moveSnake():
    global snakeSize, pausebutton, score, currentPlayer, currentScore
    canvas.pack()                                                       #packing any updates of our objects to the canvas
    positions = []                                                      #we are recording the position of snake's head here
    positions.append(canvas.coords(snake[0]))
    if positions[0][0] < 0:                                             #if snake has left the canvas from the left 
        canvas.coords(snake[0],width,
            positions[0][1],width-snakeSize,positions[0][3])            #then it wil appear from the right
    elif positions[0][2] > width:
        canvas.coords(snake[0],0-snakeSize,
            positions[0][1],0,positions[0][3])                          #dealing with the right 
    elif positions[0][3] > height:                                      #dealing with top
        canvas.coords(snake[0],
            positions[0][0],0 - snakeSize,positions[0][2],0)    
    elif positions[0][1] < 0:                                           #dealing with bottom
        canvas.coords(snake[0],
            positions[0][0],height,positions[0][2],height-snakeSize) 
    positions.clear()                                                   #for update to the snakes head position
    positions.append(canvas.coords(snake[0]))                           #appending the positions of snake's head to the data structure
    if direction == "left":
        canvas.move(snake[0], -snakeSize,0)                             #we are moving left which is why we have used the minus sign
    elif direction == "right":
        canvas.move(snake[0], snakeSize,0)
    elif direction == "up":
        canvas.move(snake[0], 0,-snakeSize)
    elif direction == "down":
        canvas.move(snake[0], 0,snakeSize)
    sHeadPos = canvas.coords(snake[0])                                  #get the snakes head position
    foodPos = canvas.coords(food)                                       #get the position of the food
    food2Pos = canvas.coords(food2)
    food3Pos = canvas.coords(food3)
    if overlapping(sHeadPos, foodPos):                                  #if the overlapping function returns true
        moveFood()                                                      #call the moveFood function
        growSnake()                                                     #call the growSnake function
    if overlapping(sHeadPos, food2Pos):
        moveFood2()
        growSnake()
    if overlapping(sHeadPos, food3Pos):
        moveFood3()
        growSnake()
    for i in range(1,len(snake)):                                       #when the head of snake overlaps other element it is game over
        if overlapping(sHeadPos, canvas.coords(snake[i])):              #if any element is overlapping
            gameOver = True
            currentScore = score                                        #saving currentScore
            saveNameNScore()
            canvas.create_text(width/2,height/2,fill="white",
                font="Times 20 italic bold", text="Game Over!")         #informing the user that the game is over
    for i in range(1,len(snake)):                                       #loop to get the positions of the remaining elements and append them to this list
        positions.append(canvas.coords(snake[i]))
    for i in range(len(snake)-1):                                       #loop to update the ith + 1 element, this will allow each element to follow the previous element
        canvas.coords(snake[i+1],positions[i][0],
            positions[i][1],positions[i][2],positions[i][3])
    if 'gameOver' not in locals() and pausebutton != True:              #preventing window.after instruction if game over
        window2.after(90, moveSnake)                                    #increasing the first parameter will decrease the speed of the game
    print(snake)
    cheatCodeMakeSnakeSmaller()

def saveNameNScore():                                                   #saving name and score in txt file
    with open("./leaderboard.txt", "a") as f:
        f.write(f"{currentPlayer + ':' + str(currentScore)}\n")
        f.close()

def placingAllFood():
    placeFood()
    placeFood2()
    placeFood3()

def placeFood():
    global food, foodX, foodY
    food = canvas.create_rectangle(0,0, snakeSize, snakeSize, fill="steel blue" )
    foodX = random.randint(0,width-snakeSize)
    foodY = random.randint(0,height-snakeSize)
    canvas.move(food, foodX, foodY)

def placeFood2():
    global food2, foodX2, foodY2
    food2 = canvas.create_rectangle(0,0, snakeSize, snakeSize, fill="purple" )
    foodX2 = random.randint(0,width-snakeSize)
    foodY2 = random.randint(0,height-snakeSize)
    canvas.move(food2, foodX2, foodY2)

def placeFood3():
    global food3, foodX3, foodY3
    food3 = canvas.create_rectangle(0,0, snakeSize, snakeSize, fill="orange" )
    foodX3 = random.randint(0,width-snakeSize)
    foodY3 = random.randint(0,height-snakeSize)
    canvas.move(food3, foodX3, foodY3)

#functions for directions of snake
def leftKey(event):
    global direction
    direction = "left"
def rightKey(event):
    global direction
    direction = "right"
def upKey(event):
    global direction
    direction = "up"
def downKey(event):
    global direction
    direction = "down"

def buttonOption1Switch():
    global Option1, Option2, window6, option1Selected
    Option1["state"] = DISABLED
    Option1["text"] = "SELECTED"
    Option2["state"] = NORMAL
    Option2["text"]="OPTION2"
    option1Button = DISABLED
    option1Selected = True

def buttonOption2Switch():
    global Option1, Option2, option1Selected
    Option2["state"] = DISABLED
    Option2["text"] = "SELECTED"
    Option1["state"] = NORMAL
    Option1["text"]="OPTION1"
    option1Selected = False 

def user_control():
    global direction 
    if option1Selected == False:
        canvas.bind("<a>", leftKey)                              #allowing user control of the snake
        canvas.bind("<d>", rightKey)
        canvas.bind("<w>", upKey)
        canvas.bind("<s>", downKey)
        canvas.focus_set()
        direction = "right"                                      #set initial direction

    elif option1Selected == True or option1Selected == "":
        canvas.bind("<Left>", leftKey)                           #allowing user control of the snake
        canvas.bind("<Right>", rightKey)
        canvas.bind("<Up>", upKey)
        canvas.bind("<Down>", downKey)
        canvas.focus_set()
        direction = "right"                                      #set initial direction

def createheadsnake():
    global snake, snakeSize, canvas
    snake = []                                                   #list where we are storing our snake objets
    snakeSize = 15
    snake.append(canvas.create_oval(snakeSize,snakeSize,snakeSize * 2, snakeSize * 2, fill="#28ff00" ))     #creating head of snake

def scoreNbuttons():
    global score, width, canvas, scoreText
    score = 0                                                     #creating score
    txt = "Score:" + str(score)
    scoreText = canvas.create_text( width/2 , 20 , fill="white",font="Times 20 italic bold", text=txt)
    pausebutton = Button(window2,  text="| |", command=pausegame, bg="#000000", foreground="#28ff00", font=("Times New Roman", 16, "bold"))
    pausebutton.place(relx=1.0, y=0, anchor="ne")

def backtomenusettingup():
    global pausebutton, window2, window3
    pausebutton = False                                           #setting pausebutton to false so it updates doing moveSnake function
    window3.destroy()                                             #destroying windows to start from 0 when calling menu
    window2.destroy()
    menu()

def continuegame():
    global window, window2, window3, pausebutton
    pausebutton = False                                           #setting pausebutton to false so it updates doing moveSnake function
    window3.withdraw()
    window2.deiconify()
    moveSnake()                                                   #calling moveSnake function again so it records our last position

def menuAfterLeaderboard():
    window4.destroy()
    window.deiconify()

def menuAfterConfigure():
    window6.withdraw() 
    window.deiconify()

def configure():
    global window6, window, Option1, Option2, option1Selected
    window.withdraw()
    configureWindow()
    backbutton = Button(window6,  text="☰", command=menuAfterConfigure, bg="#000000", foreground="#28ff00", font=("Times New Roman", 27, "bold"))
    backbutton.place(relx=1.0, y=0, anchor="ne")
    label1 =Label(window6, text="<key> commands", bg="#000000", foreground="#ffffff", font=("Times New Roman", 32, "bold"))
    label1.pack()
    label2 =Label(window6, text="Press <Return/Enter> to START the game", bg="#000000", foreground="#ffdb00", font=("Times New Roman", 11, "bold"))
    label2.pack()
    label3 =Label(window6, text="Press <Escape> for BOSSKEY", bg="#000000", foreground="#ffdb00", font=("Times New Roman", 11, "bold"))
    label3.pack()
    label4 =Label(window6, text="Press <v> in the game when score > 10 for CHEAT1", bg="#000000", foreground="#ffdb00", font=("Times New Roman", 11, "bold"))
    label4.pack()
    label5 =Label(window6, text="Press <b> in the game for CHEAT2", bg="#000000", foreground="#ffdb00", font=("Times New Roman", 11, "bold"))
    label5.pack()
    label6 =Label(window6, text="Key Configuration", bg="#000000", foreground="#ffffff", font=("Times New Roman", 31, "bold"))
    label6.pack()
    label7 =Label(window6, text="Click the option you want to play with:", bg="#000000", foreground="#ffffff", font=("Times New Roman", 11, "bold"))
    label7.pack()
    down1 = Button(window6, text= "↓", bg="#000000", foreground="#28ff00", font=("Times New Roman", 14, "bold"))
    down1.place(relx=0.5, rely=0.60, anchor=CENTER)
    up1 = Button(window6, text= "↑", bg="#000000", foreground="#28ff00", font=("Times New Roman", 14, "bold"))
    up1.place(relx=0.5, rely=0.53, anchor=CENTER)
    left1 = Button(window6, text= "←", bg="#000000", foreground="#28ff00", font=("Times New Roman", 12, "bold"))
    left1.place(relx=0.41, rely=0.57, anchor=CENTER)
    right1 = Button(window6, text= "→", bg="#000000", foreground="#28ff00", font=("Times New Roman", 12, "bold"))
    right1.place(relx=0.59, rely=0.57, anchor=CENTER)
    Option1 = Button(window6, text= "DEFAULT", command=buttonOption1Switch, bg="#000000", foreground="#28ff00", font=("Times New Roman", 12, "bold"), state= DISABLED)
    Option1.place(relx=0.5, rely=0.44, anchor=CENTER)
    down2 = Button(window6, text= "S ", command=exitbutton, bg="#000000", foreground="#28ff00", font=("Times New Roman", 12, "bold"))
    down2.place(relx=0.5, rely=0.9, anchor=CENTER)
    up2 = Button(window6, text= "W", command=exitbutton, bg="#000000", foreground="#28ff00", font=("Times New Roman", 12, "bold"))
    up2.place(relx=0.49, rely=0.83, anchor=CENTER)
    left2 = Button(window6, text= "A", command=exitbutton, bg="#000000", foreground="#28ff00", font=("Times New Roman", 12, "bold"))
    left2.place(relx=0.41, rely=0.9, anchor=CENTER)
    right2 = Button(window6, text= "D", command=exitbutton, bg="#000000", foreground="#28ff00", font=("Times New Roman", 12, "bold"))
    right2.place(relx=0.59, rely=0.9, anchor=CENTER)
    Option2 = Button(window6, text= "OPTION 2",command=buttonOption2Switch, bg="#000000", foreground="#28ff00", font=("Times New Roman", 12, "bold"))
    Option2.place(relx=0.5, rely=0.74, anchor=CENTER)
    if option1Selected == False:
        Option2["state"] = DISABLED
        Option2["text"] = "SELECTED"
        Option1["state"] = NORMAL
        Option1["text"]="OPTION1"
    emptya = Button(window6, text="", bg="#000000", foreground="#000000").place(relx=0.0, rely=0.0, anchor=NW)   #setting empty buttons to put play in the center
    emptyb = Button(window6, text="", bg="#000000", foreground="#000000").place(relx=1.0, rely=1.0, anchor=SE)
    window6.bind('<Escape>', bossKey)

def leaderboard():
    global window4, window
    window.withdraw()
    leaderboardwindow()
    label =Label(window4, text="TOP 12", bg="#08fd00", foreground="#ffffff", font=("Times New Roman", 35, "bold"))
    label.pack()
    backbutton = Button(window4,  text="☰", command=menuAfterLeaderboard, bg="#000000", foreground="#28ff00", font=("Times New Roman", 27, "bold"))
    backbutton.place(relx=1.0, y=0, anchor="ne")
    st = tkscroll.ScrolledText(window4, bg="#000000", foreground="#fbff19", font=("Times New Roman",15, "bold"))
    st.pack()
    leaderbFirstTen= openingLeaderboardFileNSorting()
    for element in leaderbFirstTen:
        st.insert(INSERT, f'{element[0]}:{element[1]}\n\n')

def openingLeaderboardFileNSorting():
    with open("./leaderboard.txt", "r") as g:
        filecontents = g.read()
        g.close()
    filelist=filecontents.splitlines()                                                  #do list of filecontents
    leaderBoardAA = {}
    for element in filelist:
        currentsplit = element.split(":")                                               #splitting when we reach :   
        user = currentsplit[0]
        score = int(currentsplit[1])
        if (user not in leaderBoardAA or score > leaderBoardAA[user]):                  #and score != "":  #we are only keeping if user is not in leaderboard or if score of user is higher
            leaderBoardAA[user] = score
    leaderBoardA = list(leaderBoardAA.items())
    leaderBoardA.sort(key=lambda element: element[1], reverse = True)                   #reverse for sorting from hightest to lowest
    leaderBoardFirstTwelve = leaderBoardA[:12]
    return leaderBoardFirstTwelve

def pausegame():
    global playbutton, window2, window3, pausebutton
    pausebutton = True
    window2.withdraw()
    pausewindow()
    playbutton = Button(window3,  text="▶", command=continuegame, bg="#000000", foreground="#28ff00", font=("Times New Roman", 16, "bold"))
    playbutton.place(relx=0.6, rely=0.5, anchor=CENTER)
    gobacktomenubutton = Button(window3,  text="☰", command=backtomenusettingup, bg="#000000", foreground="#28ff00", font=("Times New Roman", 16, "bold"))
    gobacktomenubutton.place(relx=0.4, rely=0.5, anchor=CENTER)
    savegamebutton = Button(window3, text= "Save Game", command=saveGame, bg="#000000", foreground="#28ff00", font=("Times New Roman", 16, "bold"))
    savegamebutton.place(relx=0.5, rely=0.3, anchor=CENTER)
    quitButton2 = Button(window3, text= "Exit Game", command=exitbutton, bg="#000000", foreground="#28ff00", font=("Times New Roman", 16, "bold"))
    quitButton2.place(relx=0.5, rely=0.2, anchor=CENTER)
    emptya = Button(text="").place(relx=0.0, rely=0.0, anchor=NW)   #setting empty buttons to put play in the center
    emptyb = Button(text="").place(relx=1.0, rely=1.0, anchor=SE)
    window3.bind('<Escape>', bossKey)

def menuAfterSaveGame():
    global window3
    window3.destroy()
    menu()

# this function creates a json object with the variables to save, then saves the string to a file
def saveGame():
    global width, height, quitButton, pausebutton, scoreText, txt, score
    global food, foodX, foodY, food2, foodX2, foodY2, food3, foodX3, foodY3
    global snake, snakeSize, direction, option1Selected, currentPlayer, currentScore
    # create JSON object
    jsonObject = {'var1':width, 'var2':height, 'var3':scoreText, 'var4':txt, 'var5':score, 'var6':food
    , 'var7':foodX, 'var8':foodY, 'var9':food2, 'var10':foodX2, 'var11':foodY2
    , 'var12':food3, 'var13':foodX3, 'var14':foodY3, 'var15':snake, 'var16':snakeSize
    , 'var17':direction, 'var18':option1Selected, 'var19':currentPlayer, 'var20':currentScore}
    # convert JSON object into a string     
    jsonString = json.dumps(jsonObject, indent=4)
    # open file to save string
    fileObject = open("./saveFile.json", "w")
    # save JSON string into file
    fileObject.write(jsonString)
    # reset variables to initial values
    width = ""
    height = ""
    quitButton = ""
    pausebutton = False
    scoreText = ""
    txt = ""
    score = ""
    food = ""
    foodX = ""
    foodY = ""
    food2 = ""
    foodX2 = ""
    foodY2 = ""
    food3 = ""
    foodX3 = ""
    foodY3 = ""
    snake = ""
    snakeSize = ""
    direction = ""
    option1Selected = ""
    currentPlayer = ""
    currentScore = ""
    menuAfterSaveGame()

# this function reads a json file and pints the variable values
def loadGame():
    global width, height, quitButton, pausebutton, scoreText, txt, score
    global food, foodX, foodY, food2, foodX2, foodY2, food3, foodX3, foodY3
    global snake, snakeSize, direction, option1Selected, currentPlayer, currentScore, window
    window.withdraw()
    # open file for reading
    fileObject = open("./saveFile.json", "r")
    # read string from file
    jsonContent = fileObject.read()
    # convert string into JSON object
    jsonObject = json.loads(jsonContent)
    # read values from JSON object
    width = jsonObject["var1"]
    height = jsonObject["var2"]
    scoreText = jsonObject["var3"]
    txt = jsonObject["var4"]
    score = jsonObject["var5"]
    food = jsonObject["var6"]
    foodX = jsonObject["var7"]
    foodY = jsonObject["var8"]
    food2 = jsonObject["var9"]
    foodX2 = jsonObject["var10"]
    foodY2 = jsonObject["var11"]
    food3 = jsonObject["var12"]
    foodX3 = jsonObject["var13"]
    foodY3 = jsonObject["var14"]
    snake = jsonObject["var15"]
    snakeSize = jsonObject["var16"]
    direction = jsonObject["var17"]
    option1Selected = jsonObject["var18"]
    currentPlayer = jsonObject["var19"]
    currentScore = jsonObject["var20"]
    pausegame()

def gamefunction():
    gamewindow()
    window2.bind('<Escape>', bossKey)
    createheadsnake()
    scoreNbuttons()
    placingAllFood()
    user_control()
    moveSnake()

#VARIABLES
width = ""
height = ""
quitButton = ""
pausebutton = False
scoreText = ""
txt = ""
score = ""
food = ""
foodX = ""
foodY = ""
food2 = ""
foodX2 = ""
foodY2 = ""
food3 = ""
foodX3 = ""
foodY3 = ""
snake = ""
snakeSize = ""
direction = ""
option1Selected = ""
currentPlayer = ""
currentScore = ""

#Function calling
menu()

#Images Menu
img = PhotoImage(file="freeImage.png")      
Label(window, bg = "black", foreground="black", image=img).place(x = 58, y = 305)
img2 = PhotoImage(file="snake2.png")      
Label(window, bg = "black", image=img2).place(x = 0, y = 0)   
Label(window, bg = "black", image=img2).place(x = 458, y = 0)

#blocking method, any code after this will not be executed
window.mainloop()
