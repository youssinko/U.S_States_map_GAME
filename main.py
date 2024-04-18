import turtle
from turtle import Turtle, Screen
import pandas
from scoreboard import Score
score = Score()
screen = Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Map Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_states = data["state"].to_list()

guessed_states = []
while len(guessed_states) < 50:
    text = screen.textinput(f"{len(guessed_states)}/ 50 STATES", "Name a State:").title()
    if text in data_states and text not in guessed_states:
        turtle = Turtle()
        turtle.hideturtle()
        position = data[data["state"] == text]
        turtle.penup()
        turtle.goto(int(position.x), int(position.y))
        turtle.write(text)
        score.win()
        guessed_states.append(text)
    elif text == 'Exit' or text not in data_states:
        remaining_states = []
        for x in data_states:
            if x not in guessed_states:
                remaining_states.append(x)

        new_file = pandas.DataFrame(remaining_states)
        new_file.to_csv("./remaining.csv")
        turtle.color("red")
        turtle.write("Game over", font=('FONT', 30, 'normal'), align="center")
        turtle.goto(0, 0)
        break





screen.listen()


screen.exitonclick()