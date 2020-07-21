## paddle pop game using inbuilt turtle module turtle module

import turtle
import os

try:
	sound = os.system("aplay bounce1.mp3&")
except Exception:
	import winsound
	sound = winsound.PlaySound("bounce1.mp3", winsound.SND_ASYNC)
	#sound = winsound.Beep(37, 30)
	
wn = turtle.Screen()
wn.title("PaddlePop @ DroidStudio")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)



# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dx= 1
ball.dy= 1

#Scores
score_a = 0
score_b = 0

# ScoreBoard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260), 
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier",24, "bold") )


# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 60
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 60
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 60
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 60
	paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


#Main game loop to keep the window/game running
while True:
	wn.update()
	
	# Move the ball
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)

	# Border
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		sound

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *=-1
		sound

	if ball.xcor() > 390:
		ball.setx(390)
		ball.goto(0,0)
		ball.dx *= -1
		pen.clear()
		score_a += 1
		pen.write("Player A: {} Player B: {}".format(score_a,score_b), align = "center", font = ("Courier",24, "bold") )


	if ball.xcor() < -390:
		ball.setx(-390)
		ball.goto(0,0)
		ball.dx *= -1
		score_b+=1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b), align = "center", font = ("Courier",24, "bold") )


	## Paddel bounce
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 100 and ball.ycor() > paddle_b.ycor() -100):
		ball.setx(340)
		ball.dx *= -1
		sound


	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 100 and ball.ycor() > paddle_a.ycor() -100):
		ball.setx(-340)
		ball.dx *= -1
		sound
	