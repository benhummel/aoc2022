# input = """ """  -- removed for readability 

def split_string(string):
    splitpoint = int(len(string)/2)
    c1 = string[0:splitpoint]
    c2 = string[splitpoint:]
    return c1, c2

def calculate_priority(letter):
    if letter.islower():
        priority = ord(letter) - 96
    elif letter.isupper():
        priority = ord(letter) - 38
    else:
        print("bad input probably, or something")
        return
    return priority

def get_letter_in_common(c1, c2):
    c1_uniques = set(c1)
    c2_uniques = set(c2)

    letter_in_common = str(list(c1_uniques.intersection(c2_uniques))[0])

    if letter_in_common:
        return letter_in_common
    else:
        print("no letter in common!")
        return

# do the calculations
priorities_sum = 0

for i in input.split("\n"):
    c1, c2 = split_string(i)
    letter_in_common = get_letter_in_common(c1, c2)
    priority = calculate_priority(letter_in_common)
    priorities_sum += priority

print(f"sum of all priorities is {priorities_sum}")
