import turtle 

# Create game window
wind = turtle.Screen()  # Initialize screen
wind.title("Ping Pong")  # Set window title
wind.bgcolor("#F8F8F8")  # Set background color to off-white
wind.setup(width=800, height=600)  # Set window dimensions
wind.tracer(0)  # stops the window from updating automatically

# (Player 1)
madrab1 = turtle.Turtle()
madrab1.speed(0)  # Set the speed to the highest
madrab1.shape("square")  # Set shape to square
madrab1.color("blue")  # Set color to baby blue
madrab1.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the shape 
madrab1.penup()  # stops the object from drawing lines
madrab1.goto(-350, 0)  # Set initial position (left side)

#  (Player 2)
madrab2 = turtle.Turtle()
madrab2.speed(0)  
madrab2.shape("square") 
madrab2.color("red")  
madrab2.shapesize(stretch_wid=5, stretch_len=1)  
madrab2.penup() 
madrab2.goto(350, 0)  

# Create the ball
ball = turtle.Turtle()
ball.speed(0)  
ball.shape("circle")  
ball.color("black")  
ball.penup()  
ball.goto(0, 0)  
ball.dx=3
ball.dy=-3

#score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1:0 Player2:0",align="center", font=("Courier",24,"normal"))










#Functions
def madrab1_up():
    y=madrab1.ycor() #set the y coordinate of the madrab1
    y+=20 #every time increase 20pixel
    madrab1.sety(y)

def madrab1_down():
    y=madrab1.ycor()
    y-=20 #every time decrease 20pixel
    madrab1.sety(y)

def madrab2_up():
    y=madrab2.ycor()
    y+=20 #every time increase 20pixel
    madrab2.sety(y)

def madrab2_down():
    y=madrab2.ycor()
    y-=20 #every time decrease 20pixel
    madrab2.sety(y)


#keboard bindings

wind.listen()
wind.onkeypress(madrab1_up,"w")
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")



import time

def update_game():
    wind.update() 
    move_ball()  
    wind.ontimer(update_game, 10)




# Main game 
def move_ball():
    global score1, score2
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border check ,top border +300px ,bottom border -300px,ball is 20px
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1 #reverse directions ,making +3-->-3

    if ball.ycor()<-290:#if ball is at bottom border
        ball.sety(-290)
        ball.dy*=-1    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score1+=1
        score.clear()
        score.write("Player 1:{} Player2:{}".format(score1,score2),align="center", font=("Courier",24,"normal"))  

    if ball.xcor() < -390:
         ball.goto(0, 0)
         ball.dx *= -1  
         score2 +=1
         score.clear()
         score.write("Player 1: {} Player2: {}".format(score1,score2),align="center", font=("Courier",24,"normal"))  

        
    #tasadom madrab and ball
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):

        ball.setx(340)
        ball.dx *=-1
    if (ball.xcor() < -340) and (ball.xcor() >- 350) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):

        ball.setx(-340)
        ball.dx *=-1

# Start the game
update_game()

# Keep window open
turtle.mainloop()
