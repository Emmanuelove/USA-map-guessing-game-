import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
# States = data["state"]
# State_list = States.tolist()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)



# Date_dic = {
#     "States": States,
#     "coordinates": [x_coordinates, y_coordinates]
# }


# Step 1: Convert the guess to title case
# Guessed_states = []                               # Step 5: Record the correct guesses in a list
# Run = True
# score = 0
# while Run:                                    # Step 4: Use a loop to allow the user to keep guessing
#     answer_state = (screen.textinput(title=f"{score}/50 states correct", prompt="What's another state's name?").
#                     capitalize())
#     if answer_state not in State_list:                             # Step 2: Check if the guess is among the 50 states
#         continue
#     else:
#         print(answer_state)
#         Guessed_states.append(answer_state)
#         score += 1                                      # Step 6: Keep track of the score
#         turtle.hideturtle()
#         turtle.penup()
#         state_data = data[data.state == answer_state]
#         turtle.goto(int(state_data.x), int(state_data.y))
#         turtle.write(arg=f"{answer_state}", font=("Verdana", 15, "normal"), move=False, align="center")
#
#         if score >= 15:
#             Run = False

# Step 3: Write correct guesses onto the map
