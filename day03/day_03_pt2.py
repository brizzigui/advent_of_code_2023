try:
    index_of_line = 0
    positions_num = []
    positions_symbol = []

    while True:
        line = input()
        getting_number = False

        for column, char in enumerate(line):
            if char.isnumeric() and not getting_number:
                getting_number = True
                start_column = column

            elif getting_number and not char.isnumeric():
                getting_number = False
                positions_num.append((index_of_line, start_column, index_of_line, column-1, int(line[start_column:column]))) # adiciona à lista início e fim do número

            elif getting_number and column == len(line)-1:
                getting_number = False
                positions_num.append((index_of_line, start_column, index_of_line, column, int(line[start_column:column+1]))) # adiciona à lista início e fim do número


            if not char.isalnum() and char != ".":
                positions_symbol.append((index_of_line, column))

        index_of_line += 1            

except EOFError:
    acc = 0
    for symbol in positions_symbol:
        sum_of_adjacencies = 0
        ratio = 1

        for position in positions_num:
            num_line = position[0]
            num_start = position[1]
            num_end = position[3]
            num_value = position[4]

            if symbol[0] == num_line and (symbol[1] == num_start - 1 or symbol[1] == num_end + 1):
                sum_of_adjacencies += 1
                ratio *= num_value


            elif (symbol[0] == num_line + 1 or symbol[0] == num_line - 1) and (num_start - 1) <= symbol[1] <= (num_end + 1):
                sum_of_adjacencies += 1
                ratio *= num_value

        if sum_of_adjacencies >= 2:
            acc += ratio

    print(acc)

    exit()