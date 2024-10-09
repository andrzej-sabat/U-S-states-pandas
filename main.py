import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)


def write_state_name(name, x, y):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.write(name, align="center", font=("Arial", 8, "normal"))


turtle.shape(image)
correct_guess = []
is_game_on = True
while is_game_on:
    correct_guess_count = len(correct_guess)
    all_states_count = len(data.state)

    if correct_guess_count == all_states_count:
        is_game_on = False

    answer_state = screen.textinput(title=f"{correct_guess_count}/{all_states_count} States Correct",
                                    prompt="Type another state's name").title()

    if not data[data.state == answer_state].empty and answer_state not in correct_guess:
        state_data = data[data.state == answer_state]
        state_x = int(state_data.x)
        state_y = int(state_data.y)
        write_state_name(answer_state, state_x, state_y)
        correct_guess.append(answer_state)

screen.exitonclick()
