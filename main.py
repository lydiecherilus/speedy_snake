# speedy snake game
from turtle import Turtle, Screen

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Speedy Snake")

# snake starter speed
# speed will increase each time the snake eats the food
snake_speed = 0.2

# create snake body
snake_body = Turtle("square")
snake_body.color("green")
snake_body.shapesize(stretch_len=2.5, stretch_wid=0.5)
snake_body.speed(snake_speed)

screen.exitonclick()