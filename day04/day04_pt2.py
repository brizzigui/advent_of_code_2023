try:
    index = 1
    original_matches = []
    while True:
        line = input()
        line = line.split(":")[1]

        bets, winning = line.split("|")
        bets = bets.split()
        winning = winning.split()

        points_made = 0

        for bet in bets:
            if bet in winning:
                points_made += 1

        original_matches.append((index, 1, points_made)) # middle = amount
        index += 1

except EOFError:
    acc = 0
    for i in range(len(original_matches)):
        for k in range(i+1, i+1+original_matches[i][2]):
            if k < len(original_matches):
                original_matches[k] = (original_matches[k][0], original_matches[k][1]+1*original_matches[i][1], original_matches[k][2])

    for i in range(len(original_matches)):
        acc += original_matches[i][1]

    print(acc)

    exit()