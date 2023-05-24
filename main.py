import turtle
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which tutle will win the race?\nred, blue, green, orange, "
                                                          "purple, yellow")
color = ["orange", "blue", "yellow", "green", "red", "purple"]


if user_bet:
    race_on = True
    all_turtle = []
    start_position = -100
    position = []
    for number in range(0, 6):
        new_turtle = turtle.Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color[number])
        new_turtle.goto(-230, start_position)
        all_turtle.append(new_turtle)
        position.append(start_position)
        start_position += 40
    while race_on:
        for number in range(0, 6):
            distance = random.randint(0, 10)
            all_turtle[number].forward(distance)
            if all_turtle[number].towards(230, position[number]):
                race_on = False
                winner = color[number]
                if user_bet == winner:
                    print(f"You win. The {winner} turtle won.")
                else:
                    print(f"You lose. The {winner} turtle won.")









# def create_turtle(name, position, n_color):
#     color = ["orange", "blue", "yellow", "green", "red", "purple"]
#     colour = color[n_color]
#     start = position
#     name = Turtle(shape="turtle")
#     name.color(colour)
#     name.penup()
#
#     return name.goto(x=-230, y=start)


# soba = (create_turtle("soba", -100, 0))
# dobby = (create_turtle("dobby", -60, 1))
# yukon = (create_turtle("yukon", -20, 2))
# benji = (create_turtle("benji", 20, 3))
# juneau = (create_turtle("juneau", 60, 4))
# jiw = (create_turtle("jiw", 100, 5))

screen.exitonclick()
