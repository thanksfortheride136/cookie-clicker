import turtle

wn = turtle.Screen()  #Creates window
wn.title("Cooper Cookie Clicker") #Creates screen title
wn.bgcolor("black") #sets window background color

wn. register_shape("cookie.gif") #tells turtle that theres a shape object file in the program
cookie = turtle.Turtle() #makes a cookie turtle object
cookie.shape("cookie.gif") #creates cookie object on screen
cookie.speed(0)

clicks = 0 #clicks variable, keeps track of num of clicks on cookie

pen = turtle.Turtle() #creates pen turtle object
pen.hideturtle() #We dont want to see this so we hide it
pen.color("white") #sets text color
pen.penup() #brings pen up
pen.goto(0, 400) #sends text to a certain spot on the game board (Center)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal")) #draws the text on screen, aligns text center and changes font. Uses clicked function and var.

def clicked(x, y):
    global clicks 
    clicks += 1     #global variable to access clicks outside of the function (I think)
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

cookie.onclick(clicked)  #onclick method


wn.mainloop() #I assumem this updates the window each second?