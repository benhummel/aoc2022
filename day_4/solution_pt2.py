input_split = input.split("\n")

count_pairs_overlapping = 0

for pair in input_split:  
    pair_split = pair.split(',')   # ['1-93', '2-11']
    pair_split_first = [int(x) for x in pair_split[0].split('-')]  # ['1', '93']
    pair_split_second = [int(x) for x in pair_split[1].split('-')]  # ['2', '11']

    pair_split_first_len = int(pair_split_first[1]) - int(pair_split_first[0])
    pair_split_second_len = int(pair_split_second[1]) - int(pair_split_second[0])

    if pair_split_first_len >= pair_split_second_len:
        if (pair_split_second[0] in range (pair_split_first[0], pair_split_first[1]+1)) or (pair_split_second[1] in range (pair_split_first[0], pair_split_first[1]+1)):
                count_pairs_overlapping += 1

    else:
        if (pair_split_first[0] in range (pair_split_second[0], pair_split_second[1]+1)) or (pair_split_first[1] in range (pair_split_second[0], pair_split_second[1]+1)):
            count_pairs_overlapping += 1