import numpy as np

dafaFile1 = "06/data.txt"
# dafaFile1 = "06/data_small.txt"
def load_input():
    with open(dafaFile1, "r") as f:
        return f.read().strip()
    
def part1(input):
    directions = ['^', '>', 'v', '<']

    input = input.split('\n')

    _map = []
    for i, line in enumerate(input):
        _map.append([])
        for el in line:
            _map[i].append(el)
    
    x = 0
    y = 0

    current_direction = None

    for i, line in enumerate(_map):
        for j, el in enumerate(line):
            if el in directions:
                x = i
                y = j

                current_direction = el
            
    count = 0
    finish = False
    while not finish:
        lookahead_x = x
        lookahead_y = y

        if current_direction == '^':
            lookahead_x -= 1
        elif current_direction == '>':
            lookahead_y += 1
        elif current_direction == 'v':
            lookahead_x += 1
        elif current_direction == '<':
            lookahead_y -= 1

        if lookahead_x >= 0 and lookahead_x < len(_map) and lookahead_y >= 0 and lookahead_y < len(_map[0]) and _map[lookahead_x][lookahead_y] == '#':
            if current_direction == '^':
                current_direction = '>'
            elif current_direction == '>':
                current_direction = 'v'
            elif current_direction == 'v':
                current_direction = '<'
            elif current_direction == '<':
                current_direction = '^'
        else:
            x = lookahead_x
            y = lookahead_y

        if lookahead_x < 0 or lookahead_x >= len(_map) or lookahead_y < 0 or lookahead_y >= len(_map[0]):
            count += 1
            finish = True
            break

        if _map[x][y] == '.':
            count += 1
            _map[x][y] = 'X'

    return count


def part2(input):
    directions = ['^', '>', 'v', '<']

    input = input.split('\n')

    _map = []
    for i, line in enumerate(input):
        _map.append([])
        for el in line:
            _map[i].append(el)
    
    x = 0
    y = 0

    current_direction = None

    for i, line in enumerate(_map):
        for j, el in enumerate(line):
            if el in directions:
                x = i
                y = j

                current_direction = el
            
    loops = 0
    reset_guard_x = x
    reset_guard_y = y
    reset_direction = current_direction
    for i, line in enumerate(_map):
        index = i

        for j, el in enumerate(line):
            if el != '#' and el not in directions:
                _map[index][j] = '#'

                direction_change_map = []
                for k, line in enumerate(_map):
                    direction_change_map.append([])
                    for el in line:
                        direction_change_map[k].append(0)

                finish = False
                while not finish:
                    lookahead_x = x
                    lookahead_y = y

                    if current_direction == '^':
                        lookahead_x -= 1
                    elif current_direction == '>':
                        lookahead_y += 1
                    elif current_direction == 'v':
                        lookahead_x += 1
                    elif current_direction == '<':
                        lookahead_y -= 1

                    if lookahead_x >= 0 and lookahead_x < len(_map) and lookahead_y >= 0 and lookahead_y < len(_map[0]) and _map[lookahead_x][lookahead_y] == '#':
                        if current_direction == '^':
                            current_direction = '>'
                        elif current_direction == '>':
                            current_direction = 'v'
                        elif current_direction == 'v':
                            current_direction = '<'
                        elif current_direction == '<':
                            current_direction = '^'

                        direction_change_map[x][y] += 1
                        if direction_change_map[x][y] == 4:
                            loops += 1
                            finish = True
                    else:
                        x = lookahead_x
                        y = lookahead_y

                    if lookahead_x < 0 or lookahead_x >= len(_map) or lookahead_y < 0 or lookahead_y >= len(_map[0]):
                        finish = True

                _map[index][j] = '.'

                for k, line in enumerate(_map):
                    for l, el in enumerate(line):
                        if el in directions:
                            _map[k][l] = '.'

                _map[reset_guard_x][reset_guard_y] = reset_direction
                x = reset_guard_x
                y = reset_guard_y
                current_direction = reset_direction

    return loops


def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()