#data
def get_lines():
    with open('input.txt') as file:
        return file.read().splitlines()
    
lines = get_lines()

def get_games(input):
     
     games = input.split(': ')[1].split('; ')

     games = [i.split(', ') for i in games]

     #flatten
     return [item for row in games for item in row]

def test_game(input):

    input = input.split(' ')

    if input[1] == 'blue' and int(input[0]) <= 14:
        return True
    elif input[1] == 'green' and int(input[0]) <= 13:
        return True
    elif input[1] == 'red' and int(input[0]) <= 12:
        return True
    else:
        return False
    
#part 1
value = 0
for i in range(len(lines)):
    
    games = get_games(lines[i])

    if all([test_game(game) for game in games]):
        value += i + 1

#2149

#part 2

#find minimum red, green, blue 

def find_minimum(games):

    red = 0
    green = 0
    blue = 0

    for i in games:
        i = i.split(' ')

        if i[1] == 'blue':
            if int(i[0]) > blue:
                blue = int(i[0])
        elif i[1] == 'green':
            if int(i[0]) > green:
                green = int(i[0])
        elif i[1] == 'red':
            if int(i[0]) > red:
                red = int(i[0])
    
    return red*green*blue

value = 0
for i in lines:
    value += (find_minimum(get_games(i)))

#71274