from turtle import Turtle, Screen
from Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("ping pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen_ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(screen_ball.speed)
    screen.update()
    screen_ball.move()

    if screen_ball.ycor() > 280 or screen_ball.ycor() < -280:
        screen_ball.bounce_y()

    if screen_ball.distance(r_paddle) < 50 and screen_ball.xcor() > 320 or screen_ball.distance(
            l_paddle) < 50 and screen_ball.xcor() < -320:
        screen_ball.bounce_x()

    if screen_ball.xcor() > 380:
        screen_ball.reset()
        scoreboard.l_point()

    if screen_ball.xcor() < -380:
        screen_ball.reset()
        scoreboard.r_point()

screen.exitonclick()