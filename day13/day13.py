with open(r'input.txt') as file:
    timestamp = int(file.readline())
    busses = [(idx, int(bus)) for idx, bus in enumerate(file.readline().split(",")) if bus != 'x']

def part1(timestamp, busses):
    minBusTime, bus = min([(bus - timestamp % bus, bus) for _, bus in busses])
    return minBusTime * bus

def part2(departure, busses):
    _, period = busses[0]
    t = 0
    for busIdx, bus in busses[1:]:
        offset = None
        while True:
            if (t + busIdx) % bus == 0:
                if offset is None:
                    offset = t
                else:
                    period = t - offset
                    break

            t += period

    return offset

print(part1(timestamp, busses))
print(part2(timestamp, busses))
