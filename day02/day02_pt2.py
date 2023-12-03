try:
    index = 1
    sum_of_products = 0

    while True:
        line = input()
        line = line[line.find(":")+1:]
        line = line.split(";")

        blue_cubes = 1
        red_cubes = 1
        green_cubes = 1
        
        for game in line:
            game = game.split(",")

            for play in game:
                for string in ["blue", "red", "green"]:
                    if play.find(string) != -1:
                        color = string  
                        
                number_cubes = int(play.split()[0]) # estará sempre nesse índice

                if color == "blue":
                    blue_cubes = max(number_cubes, blue_cubes)

                elif color == "red":
                    red_cubes = max(number_cubes, red_cubes)

                else:
                    green_cubes = max(number_cubes, green_cubes)  

        product = blue_cubes*red_cubes*green_cubes
        sum_of_products += product
        
        index += 1
    

except EOFError:
    print(sum_of_products)
    exit()