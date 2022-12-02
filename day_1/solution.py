import numpy as np 

# input_string = [...]
# removed for readability

# import the string, look for any instance of 2 new lines and split on it. 
# this creates 1 list entry per elf
s = input_string.split("\n\n")

# within each elf's list, separate out each calory entry as a separate list item
s_clean = []
for i in s:
    s_clean.append(i.split("\n"))

outputs_list = []

# sum up each elf's list of calories
for elf_num, calories_list in enumerate(s_clean):
    outputs_list.append(np.array(calories_list).astype('int32').sum())

# get top 3
top_3_values = []
for i in range(3):
    current_max_value = max(outputs_list)
    top_3_values.append(current_max_value)
    # remove max value from list
    outputs_list.remove(current_max_value)


# part 1 solution
part_1_solution = top_3_values[0]

# part 2 
part_2_solution = sum(top_3_values)