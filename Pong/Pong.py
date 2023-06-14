import turtle
import winsound

#window setup
window = turtle.Screen()
window.title("Turtle Pong")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#Score
scoreA=0
scoreB=0


#Paddle A
paddleA=turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)

#Paddle B
paddleB=turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.15
ball.dy=0.15

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0 | Player 2: 0",align="center",font=("Courier",24,"normal"))


#Functions
#A
def PadA_up():
    y=paddleA.ycor()
    y+=20
    paddleA.sety(y)

def PadA_down():
    y=paddleA.ycor()
    y-=20
    paddleA.sety(y)
#B
def PadB_up():
    y=paddleB.ycor()
    y+=20
    paddleB.sety(y)

def PadB_down():
    y=paddleB.ycor()
    y-=20
    paddleB.sety(y)

#Keyboard Binding
window.listen()
window.onkeypress(PadA_up,"w")
window.onkeypress(PadA_down,"s")
window.onkeypress(PadB_up,"Up")
window.onkeypress(PadB_down,"Down")

#main game loop
while True:
    window.update()
    
    #ball move
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(scoreA,scoreB),align="center",font=("Courier",24,"normal"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(scoreA,scoreB),align="center",font=("Courier",24,"normal"))
        
    #collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)