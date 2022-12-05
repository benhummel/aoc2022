input_split = input.split("\n")

count_pairs_overlapping = 0

for pair in input_split:  
    pair_split = pair.split(',')   # ['1-93', '2-11']
    pair_split_first = [int(x) for x in pair_split[0].split('-')]  # ['1', '93']
    pair_split_second = [int(x) for x in pair_split[1].split('-')]  # ['2', '11']

    # figure out which of the pair is a larger set. if they're equal, pick the first. 
    pair_split_first_len = int(pair_split_first[1]) - int(pair_split_first[0])
    pair_split_second_len = int(pair_split_second[1]) - int(pair_split_second[0])

    if pair_split_first_len >= pair_split_second_len:
        # check if the first pair's lower number is lower than the second pair's lower number
        # check if the first pair's higher number is higher than the second pair's higher number
        if (pair_split_first[0] <= pair_split_second[0]) and ((pair_split_first[1] >= pair_split_second[1])):
            count_pairs_overlapping += 1
    else:
        if (pair_split_second[0] <= pair_split_first[0]) and ((pair_split_second[1] >= pair_split_first[1])):
            count_pairs_overlapping += 1

print(count_pairs_overlapping)