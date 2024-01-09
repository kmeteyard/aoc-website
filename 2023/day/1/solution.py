
#data
def get_lines():
    with open('input.txt') as file:
        return file.read().splitlines()
    
lines = get_lines()

#part 1

digits = [[digit for digit in string if digit.isdigit()] for string in lines]

values = [i[0] + i[len(i)-1] for i in digits]

sum(int(i) for i in values)

#54450

#part 2

#Bit ugly - could also find the position of each number
#in a string and resolve accordingly

def digit_replace(s):

    s = s.replace('one', 'o1e')
    s = s.replace('two', 't2o')
    s = s.replace('three', 't3e')
    s = s.replace('four', 'f4r')
    s = s.replace('five', 'f5e')
    s = s.replace('six', 's6x')
    s = s.replace('seven', 's7n')
    s = s.replace('eight', 'e8t')
    s = s.replace('nine', 'n9e')

    return s

part2 = [digit_replace(i) for i in lines]

digits = [[digit for digit in string if digit.isdigit()] for string in part2]

values = [i[0] + i[len(i)-1] for i in digits]

sum(int(i) for i in values)

#54265