# rock paper scissors
# round 2!

# input = """B Z, B Z...""" 
# removed for readability

# create 1 list item out of each row 
input_list = input.split("\n")

# should have just done something like this the first time i think
all_moves = {
    "rock": {
        "beats": "scissors",
        "beaten_by": "paper",
        "score": 1,
    },
    "paper": {
        "beats": "rock",
        "beaten_by": "scissors",
        "score": 2,
    },
    "scissors": {
        "beats": "paper",
        "beaten_by": "rock",
        "score": 3,
    }
}

# function to convert a letter, like "X", into its actual play, like "rock"
# there's definitely a cleaner way to do this
def convert_letter_to_rps(letter):
    if letter == "A":
        rps = "rock"
    elif letter == "B":
        rps = "paper"
    elif letter == "C":
        rps = "scissors"
    else:
        raise ValueError("error converting input to RPS!")
        return
    return rps

# calculate who wins or if it's a draw
def calculate_this_round_outcome(opponent_choice_rps, my_choice_rps):
    if my_choice_rps == opponent_choice_rps:
        outcome = "draw"
    elif opponent_choice_rps == all_moves[my_choice_rps]["beaten_by"]:
        outcome = "opponent"
    elif opponent_choice_rps == all_moves[my_choice_rps]["beats"]:
        outcome = "me"

    return outcome

def figure_out_my_move(opponent_choice_rps, desired_outcome):
    my_ideal_move = ""
    
    if desired_outcome == "Y":
        my_ideal_move = opponent_choice_rps
    elif desired_outcome == "X":  # i lose 
        my_ideal_move = all_moves[opponent_choice_rps]["beats"]
    elif desired_outcome == "Z": # i win
        my_ideal_move = all_moves[opponent_choice_rps]["beaten_by"]

    return(my_ideal_move)

# calculate the scores for each player of the round
def calculate_this_round_score(opponent_choice_rps, my_choice_rps):

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
    
    opponent_points += all_moves[opponent_choice_rps]['score']
    my_points += all_moves[my_choice_rps]['score']

    return opponent_points, my_points



# play the game!

opponent_score_total = 0
my_score_total = 0

for i in input_list:
    opponent_choice, desired_outcome = i.split(" ")  # "A Z" becomes ["A", "Z"]

    opponent_choice_rps = convert_letter_to_rps(opponent_choice)
    my_choice_rps = figure_out_my_move(opponent_choice_rps, desired_outcome)

    opponent_points, my_points = calculate_this_round_score(opponent_choice_rps, my_choice_rps)
    
    opponent_score_total += opponent_points
    my_score_total += my_points

print(f"my_score_total:  {my_score_total}")
print(f"opponent_score_total:  {opponent_score_total}")