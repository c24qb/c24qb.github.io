import turtle


window = turtle.Screen()
window._root.attributes('-topmost', 1)
window._root.attributes('-topmost', 0)
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

ball = turtle.Turtle("circle")
ball.penup()
ball.speed(0)
ball.color("white")
ball.goto(0, 0)

paddle_a = turtle.Turtle("square")
paddle_a.shapesize(5,1)
paddle_a.penup()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.goto(-360, 0)

paddle_b = turtle.Turtle("square")
paddle_b.shapesize(5,1)
paddle_b.penup()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.goto(360, 0)

window.listen()

def paddle_a_up():
	old_y_cor = paddle_a.ycor()
	paddle_a.sety(old_y_cor + 10)


def paddle_a_down():
	old_y_cor = paddle_a.ycor()
	paddle_a.sety(old_y_cor - 10)

def paddle_b_up():
	old_y_cor = paddle_b.ycor()
	paddle_b.sety(old_y_cor + 10)


def paddle_b_down():
	old_y_cor = paddle_b.ycor()
	paddle_b.sety(old_y_cor - 10)

window.onkey(paddle_a_up, "w")
window.onkey(paddle_a_down, "s")
window.onkey(paddle_b_up, "Up")
window.onkey(paddle_b_down, "Down")

ball_should_be_moving_up = True
ball_should_be_moving_left = True


while True:
	window.update()
	if ball_should_be_moving_up == True:
		old_y_cor = ball.ycor()
		ball.sety(old_y_cor + 2)
	else:
		old_y_cor = ball.ycor()
		ball.sety(old_y_cor - 2)
	if ball_should_be_moving_left == True:
		old_x_cor = ball.xcor()
		ball.setx(old_x_cor - 2)
	else: 
		old_x_cor = ball.xcor()
		ball.setx(old_x_cor + 2)
	if ball.ycor() == 300:
		ball_should_be_moving_up = False
	if ball.xcor() == paddle_a.xcor() and ball.ycor() >= paddle_a.ycor() - 50 and ball.ycor() <= paddle_a.ycor() + 50:
		ball_should_be_moving_left = False
	if ball.ycor() == -300:
		ball_should_be_moving_up = True
	if ball.xcor() == paddle_b.xcor() and ball.ycor() >= paddle_b.ycor() - 50 and ball.ycor() <= paddle_b.ycor() + 50:
		ball_should_be_moving_left = True
	if ball.xcor() < -400:
		ball.goto(0, 0)
	if ball.xcor() > 400:
		ball.goto(0, 0)
