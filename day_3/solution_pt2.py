# input = """ """  -- removed for readability 

def calculate_priority(letter):
    if letter.islower():
        priority = ord(letter) - 96
    elif letter.isupper():
        priority = ord(letter) - 38
    else:
        print("bad input probably, or something")
        return
    return priority

def get_letter_in_common(elf1, elf2, elf3):
    elf1_uniques = set(elf1)
    elf2_uniques = set(elf2)
    elf3_uniques = set(elf3)

    letter_in_common = str(list(elf1_uniques & elf2_uniques & elf3_uniques)[0])

    if letter_in_common:
        return letter_in_common
    else:
        print("no letter in common!")
        return


l = input.split("\n")

# split elves into trios
# make a list of lists, where each sub-list is a trio
this_trio = []
list_of_elf_trios = []

for i in range(len(l)):
    # check if we should start a new list
    print(f"{i}: {l[i]}")
    if ((i % 3 == 0) & (i > 0)):
        list_of_elf_trios.append(this_trio.copy())
        this_trio.clear()
    elif i == len(l) - 1:
        this_trio.append(l[i])
        list_of_elf_trios.append(this_trio.copy())
    this_trio.append(l[i])

# do the calculations
priorities_sum = 0

for trio in list_of_elf_trios:
    letter_in_common = get_letter_in_common(trio[0], trio[1], trio[2])
    priority_score = calculate_priority(letter_in_common)
    priorities_sum += priority_score
print(priorities_sum)