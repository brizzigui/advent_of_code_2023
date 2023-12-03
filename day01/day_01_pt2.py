try:
    total = 0

    while True: 
        line = input()
        lowest_index = len(line)
       
        for value, sub in enumerate(["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], 1):
            index = line.find(sub)
            if index == -1:
                continue

            if index < lowest_index:
                lowest_index = index
                first = str(value) if value < 10 else str(value - 9)

        line = line[::-1]
        lowest_index = len(line)

        for value, sub in enumerate(["1", "2", "3", "4", "5", "6", "7", "8", "9", "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"], 1):
            index = line.find(sub)
            if index == -1:
                continue

            if index < lowest_index:
                lowest_index = index
                second = str(value) if value < 10 else str(value - 9)

        num = first + second
        num = int(num)
        total += num

except EOFError:
    print(total)
    exit()