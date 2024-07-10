import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

data = pandas.read_csv("india_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct", prompt="What's the next state "
                                                                                             "name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        # t.hideturtle()
        state_data = data[data["state"] == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
