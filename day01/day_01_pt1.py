try:
    total = 0

    while True:
        line = input()

        first = 0
        first_went = False
        second = 0
        second_went = False


        for i in range(len(line)):
            if line[i].isnumeric() and not first_went:
                first = line[i]
                first_went = True

            if line[len(line)-i-1].isnumeric() and not second_went:
                second = line[len(line)-i-1] 
                second_went = True

        num = first + second
        num = int(num)
        total += num


except EOFError:
    print(total)
    exit()