'''
--- Day 12: Rain Risk ---

Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

For example:

F10
N3
F7
R90
F11

These instructions would be handled as follows:

    F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
    N3 would move the ship 3 units north to east 10, north 3.
    F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
    R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
    F11 would move the ship 11 units south to east 17, south 8.

At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?

Your puzzle answer was 1032.
--- Part Two ---

Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    Action F means to move forward to the waypoint a number of times equal to the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

For example, using the same instructions as above:

    F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
    N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
    F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
    R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
    F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.

After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?

Your puzzle answer was 156735.
'''


import math
with open(r'input.txt') as file:
    lines = [{'op': line[0], 'val': int(line[1:])} for line in file.read().strip().split()]

# MOVES = {
#     'N': complex(0, 1),
#     'E': complex(1, 0),
#     'S': complex(0, -1),
#     'W': complex(-1, 0)
# }
#
# ROTATION = 1j
# NS, EW = [], []
# current = (0 + 0j)
#
# def next(z, op, val):
#     real, img = z.real, z.imag
#     direction = -1 if atan2(img, real) < 0 else 1
#
#     if (op == 'F'):
#         return z + (val + 0j)
#
#     if op in ['L', 'R']:
#         rotation_vector = direction * ROTATION ** (val // 90)
#         return z * rotation_vector
#
#     if op in ['N', 'S']:
#         return z + complex(0, direction * val)
#
#     if op in ['E', 'W']:
#         return z + complex(direction * val, 0)
#
# for index, line in lines.items():
#     if current == complex(0, 0):
#         if line['op'] == 'W':
#             current = (-line['val'] + 0j)
#             continue
#         elif line['op'] == 'N':
#             current = complex(0, line['val'])
#             continue
#         elif line['op'] == 'S':
#             current = complex(0, -line['val'])
#             continue
#         elif line['op'] == 'F':
#             current = (line['val'] + 0j)
#             continue
#
#     current = next(current, line['op'], line['val'])
#
# print(abs(current.real) + abs(current.imag))

class Ship:

    def __init__(self):
        self.degree = 0
        self.x = 0
        self.y = 0

    def gotoF(self, unit):
        if self.degree == 90:
            self.gotoE(unit)
        if self.degree == 180:
            self.gotoS(unit)
        if self.degree == 0:
            self.gotoN(unit)
        if self.degree == 270:
            self.gotoW(unit)

    def gotoN(self, unit):
        self.x += unit

    def gotoS(self, unit):
        self.x -= unit

    def gotoW(self, unit):
        self.y -= unit

    def gotoE(self, unit):
        self.y += unit

    def rotate(self, newDegree):
        self.degree = (self.degree + newDegree) % 360

    def rotateL(self, degree):
        self.rotate(-degree)

    def rotateR(self, degree):
        self.rotate(degree)

    def manhattanDist(self):
        return abs(self.x) + abs(self.y)


class Ship2(Ship):
    def __init__(self):
        super(Ship2, self).__init__()
        self.x_ship = 0
        self.y_ship = 0

    def gotoF2(self, unit):
        self.x_ship += self.x * unit
        self.y_ship += self.y * unit


    def rotate(self, degree):
        radiant = (degree * math.pi) / 180
        new_x = int(math.cos(radiant) * self.x + math.sin(radiant) * self.y)
        new_y = int(-math.sin(radiant) * self.x + math.cos(radiant) * self.y)

        self.x, self.y = new_x, new_y


ship = Ship()
ship.rotate(90)
for line in lines:
    op, val = line['op'], line['val']

    if op == 'F':
        ship.gotoF(val)
    elif op == 'N':
        ship.gotoN(val)
    elif op == 'E':
        ship.gotoE(val)
    elif op == 'S':
        ship.gotoS(val)
    elif op == 'W':
        ship.gotoW(val)
    elif op == 'R':
        ship.rotateR(val)
    elif op == 'L':
        ship.rotateL(val)

print(ship.manhattanDist()) # 1032

ship = Ship2()
ship.x = 1
ship.y = 10
ship.rotate(-90)

wpx = 10
wpy = 1
posx = 0
posy = 0

for line in lines:
    op, val = line['op'], line['val']

    if op == 'F':
        ship.gotoF2(val)
    elif op == 'N':
        ship.gotoN(val)
    elif op == 'E':
        ship.gotoE(val)
    elif op == 'S':
        ship.gotoS(val)
    elif op == 'W':
        ship.gotoW(val)
    elif op == 'R':
        ship.rotateR(val)
    elif op == 'L':
        ship.rotateL(val)

    print(ship.x, ship.y, ship.x_ship, ship.y_ship, ship.degree)

    d, n = line['op'], line['val']
    if d == "N":
        wpy += n
    elif d == "S":
        wpy -= n
    elif d == "E":
        wpx += n
    elif d == "W":
        wpx -= n
    elif d in ("R", "L") and n == 180:
        wpx, wpy = -wpx, -wpy
    elif d == "R":
        if n == 90:
            wpx, wpy = wpy, -wpx
        elif n == 270:
            wpx, wpy = -wpy, wpx
    elif d == "L":
        if n == 90:
            wpx, wpy = -wpy, wpx
        elif n == 270:
            wpx, wpy = wpy, -wpx
    elif d == "F":
        posx += n * wpx
        posy += n * wpy

    print(wpy, wpx, posy, posx)

print(abs(ship.x_ship) + abs(ship.y_ship))

# for line in lines:
#     d, n = line['op'], line['val']
#     if d == "N":
#         wpy += n
#     elif d == "S":
#         wpy -= n
#     elif d == "E":
#         wpx += n
#     elif d == "W":
#         wpx -= n
#     elif d in ("R", "L") and n == 180:
#         wpx, wpy = -wpx, -wpy
#     elif d == "R":
#         if n == 90:
#             wpx, wpy = wpy, -wpx
#         elif n == 270:
#             wpx, wpy = -wpy, wpx
#     elif d == "L":
#         if n == 90:
#             wpx, wpy = -wpy, wpx
#         elif n == 270:
#             wpx, wpy = wpy, -wpx
#     elif d == "F":
#         posx += n * wpx
#         posy += n * wpy
#
#     print(wpy, wpx, posy, posx)

print(abs(posx) + abs(posy)) # 156735


