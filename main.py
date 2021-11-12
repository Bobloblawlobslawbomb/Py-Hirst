from turtle import Screen, Turtle, colormode
from random import randint, choice

timmy = Turtle()
timmy.speed("fastest")

colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


rgb_values = []

for _ in range(7):
    r_g_b = random_color()
    rgb_values.append(r_g_b)

x = -628
y = -522

timmy.hideturtle()
timmy.color(255, 255, 255)
timmy.setpos(x, y)

for _ in range(22):
    for _ in range(26):
        timmy.dot(20, choice(rgb_values))
        timmy.penup()
        timmy.forward(50)
    y += 50
    timmy.setpos(x, y)

screen = Screen()
screen.exitonclick()
