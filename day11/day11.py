from copy import deepcopy

with open(r'input.txt') as file:
    lines = [line for line in file.read().strip().split()]


def part1(matrix):
    rows, columns = len(matrix), len(matrix[0])
    neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    itr = 1

    while True:
        copy = [''] * rows
        for row in range(rows):
            for col in range(columns):
                x0 = matrix[row][col]

                if x0 == '.':
                    copy[row] += '.'
                elif x0 == '#':
                    total = sum([(0 < row - l < rows) and
                                         (0 < col - m < columns) and
                                         (matrix[row - l][col - m] == '#') for l, m in neighbours])
                    copy[row] += '#' if total < 4 else 'L'
                else:
                    for l, m in neighbours:
                        if (0 < row - l < rows) and \
                                (0 < col - m < columns) and \
                                (matrix[row - l][col - m] == '#'):
                            copy[row] += 'L'
                            continue

                        copy[row] += '#'

        if copy == matrix:
            break

        itr += 1
        matrix = deepcopy(copy)

    return sum([line.count('#') for line in lines]), itr


print(part1(lines))
