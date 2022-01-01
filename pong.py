# Simple pong game in python3
# By @JKrecisz

import turtle

# Player setup
score_player_a, score_player_b = 0, 0

platform = int(input("What platform do you use (1 - windows, 2 - linux, 3 - mac)?\nPlatform: "))
if platform == 1:
    import winsound
    def bounceSound():
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
elif platform == 2:
    import os
    def bounceSound():
        os.system("aplay bounce.wav&")
else:
    import os
    def bounceSound():
        os.system("afplay bounce.wav&")

print("\n\n- 1 - easy\n- 2 - medium\n- 3 - hard\n")
difficulty = int(input("Difficulty: "))

# Window Setup
window = turtle.Screen()
window.title("Pong game by @JKrecisz")
window.bgcolor("black")
window.setup(width=1000, height=800)
window.tracer(0)

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-450, 0)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(450, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

if difficulty == 3:
    ball.dx = 12
    ball.dy = -12
elif difficulty == 2:
    ball.dx = 9
    ball.dy = -9
else:
    ball.dx = 7
    ball.dy = -7

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 350)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 26, "normal"))

# Function
def paddle1_up():
    y = paddle1.ycor()
    if y <= 320:
        y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    if y >= -320:
        y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    if y <= 320:
        y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    if y >= -320:
        y -= 20
    paddle2.sety(y)

# Keyboard biding
window.listen()
window.onkeypress(paddle1_up, "w")
window.onkeypress(paddle1_down, "s")
window.onkeypress(paddle2_up, "Up")
window.onkeypress(paddle2_down, "Down")

# Main
while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > (window.window_height()/2)-20:
        ball.dy *= -1
        bounceSound()


    if ball.ycor() < -((window.window_height()/2)-20):
        ball.dy *= -1
        bounceSound()

    if ball.xcor() > (window.window_width()/2)-20:
        ball.goto(0, 0)
        ball.dx *= -1
        score_player_a += 1

    if ball.xcor() < -((window.window_width()/2)-20):
        ball.goto(0, 0)
        ball.dx *= -1
        score_player_b += 1

    # Paddle and ball colisions
    if (ball.xcor() > 450 and ball.xcor() < 470) and (ball.ycor() < paddle2.ycor() + 52 and ball.ycor() > paddle2.ycor() - 52):
        ball.setx(430)
        ball.dx *= -1
        bounceSound()

    if (ball.xcor() < -450 and ball.xcor() > -470) and (ball.ycor() < paddle1.ycor() + 52 and ball.ycor() > paddle1.ycor() - 52):
        ball.setx(-430)
        ball.dx *= -1
        bounceSound()

    # Displaying score
    pen.clear()
    pen.write(f"Player A: {score_player_a}   Player B: {score_player_b}", align="center", font=("Courier", 24, "normal"))