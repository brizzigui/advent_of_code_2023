try:
    index = 1
    sum_of_index = 0

    while True:
        invalid = False
        line = input()
        line = line[line.find(":")+1:]
        line = line.split(";")
        
        for game in line:
            blue_cubes = 0
            red_cubes = 0
            green_cubes = 0

            game = game.split(",")

            for play in game:
                for string in ["blue", "red", "green"]:
                    if play.find(string) != -1:
                        color = string  
                        
                number_cubes = int(play.split()[0]) # estará sempre nesse índice

                if color == "blue":
                    blue_cubes += number_cubes

                elif color == "red":
                    red_cubes += number_cubes

                else:
                    green_cubes += number_cubes


            if not (blue_cubes <= 14 and red_cubes <= 12 and green_cubes <= 13):
                invalid = True
        
        if not invalid:
            sum_of_index += index
        
        index += 1
    

except EOFError:
    print(sum_of_index)
    exit()