# rock paper scissors pt 1 

# input = """B Z, B Z...""" 
# removed for readability

# create 1 list item out of each row 
input_list = input.split("\n")

# function to convert a letter, like "X", into its actual play, like "rock"
def convert_letter_to_rps(letter):
    if letter in ["A", "X"]:
        rps = "rock"
    elif letter in ["B", "Y"]:
        rps = "paper"
    elif letter in ["C", "Z"]:
        rps = "scissors"
    else:
        raise ValueError("error converting input to RPS!")
        return
    return rps

# calculate who wins or if it's a draw
def calculate_this_round_outcome(opponent_choice_rps, my_choice_rps):

    opponent_win_combos = [
        ("rock", "scissors"), 
        ("scissors", "paper"), 
        ("paper", "rock")
    ]

    if my_choice_rps == opponent_choice_rps:
        outcome = "draw"
    elif (opponent_choice_rps, my_choice_rps) in opponent_win_combos:
        outcome = "opponent"
    else:
        outcome = "me"

    return outcome

# calculate the scores for each player of the round
def calculate_this_round_score(opponent_choice, my_choice):
    if (opponent_choice not in ["A", "B", "C"]) or (my_choice not in ["X", "Y", "Z"]):
        raise ValueError("Bad input")
        return

    opponent_choice_rps = convert_letter_to_rps(opponent_choice)
    my_choice_rps = convert_letter_to_rps(my_choice)

    scores_dict = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }

    opponent_points = 0
    my_points = 0

    outcome = calculate_this_round_outcome(opponent_choice_rps, my_choice_rps)

    if outcome == "me":
        my_points += 6
    elif outcome == "opponent":
        opponent_points += 6
    else:  #draw
        my_points += 3
        opponent_points += 3
    
    opponent_points += scores_dict[opponent_choice_rps]
    my_points += scores_dict[my_choice_rps]

    return opponent_points, my_points



# play the game!

opponent_score_total = 0
my_score_total = 0

for i in input_list:
    opponent_choice, my_choice = i.split(" ")  # "A Z" becomes ["A", "Z"]

    opponent_points, my_points = calculate_this_round_score(opponent_choice, my_choice)
    
    opponent_score_total += opponent_points
    my_score_total += my_points

print(f"my_score_total:  {my_score_total}")
print(f"opponent_score_total:  {opponent_score_total}")