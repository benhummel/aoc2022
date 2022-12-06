# crates = """[Q]         [N]             [N]"""
# instructions = """move 3 from 6 to 2..."""

 # fill empty spaces with xxx
cr = crates.replace("    ", " xxx")
crs = cr.split('\n')
crs

def get_top_crate(column, crate_table):
    # returns an int with the first row from the top that contains a crate
    # for a given column. Answer is 1-indexed to match the input. 
    for i in range(len(crate_table)):
        row = crate_table[i]
        if row[column] != 'xxx':
            return i, row[column]
        elif i == len(crate_table) - 1:
            return -1, 'xxx'

instructions_split = instructions.split('\n')

crs_cells = []
for i in crs:
    i_split = i.split(' ')
    crs_cells.append(i_split)
crs_cells = crs_cells[:8]

# parse data from each line of instructions
# for i in instructions_split:
for row in crs_cells:
    print(row)
for counter, instruction in enumerate(instructions_split):
    num_boxes = int(instruction.split(' from ')[0].split('move ')[1])
    from_crate_column = int(instruction.split(' from ')[1].split(' to ')[0]) - 1
    to_crate_column = int(instruction.split(' from ')[1].split(' to ')[1]) - 1

    # do a loop on number of boxes to move 
    for i in range(num_boxes):   
        # "from 6"
        # identify the top crate and position from row 6, index 5
        from_top_crate_row, from_top_crate_value = get_top_crate(from_crate_column, crs_cells)
        if from_top_crate_row != -1: # -1 means there are no crates to move in this column, so we skip
            # "to 2"
            # identify the top crate and position
            to_top_crate_row, to_top_crate_value = get_top_crate(to_crate_column, crs_cells)

            # if there's already a crate in the top row of the TO column, we add a new row
            if to_top_crate_row == 0:
                crs_cells.insert(0, ['xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx'])
                to_insert_row = 0
                from_top_crate_row += 1
                
            # in the "to" column, go up 1 row and insert whatever is in the from box position
            # [row][column]
            elif to_top_crate_row == -1:
                to_insert_row = len(crs_cells)-1 # the bottom row
            else:
                to_insert_row = to_top_crate_row - 1  # insert into the one above the top crate

            crs_cells[to_insert_row][to_crate_column] = from_top_crate_value

            # remove the value from the from box and replace with 'xxx'
            crs_cells[from_top_crate_row][from_crate_column] = 'xxx'
        else:
            print(f"from column as no crates, skip")
        
        if crs_cells[0] == ['xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx']:
            crs_cells.pop(0) # remove empty rows at the top if they exist

top_crates = ""
for i in range(9):
    top_crates = top_crates + get_top_crate(i, crs_cells)[1][1]
print(top_crates)