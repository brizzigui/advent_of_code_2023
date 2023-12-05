try:
    total_points = 0
    while True:
        line = input()
        line = line.split(":")[1]

        bets, winning = line.split("|")
        bets = bets.split()
        winning = winning.split()

        points_made = 0

        for bet in bets:
            if bet in winning:
                if points_made == 0:
                    points_made = 1
                
                else:
                    points_made *=2

        total_points += points_made


except EOFError:
    print(total_points)
    exit()