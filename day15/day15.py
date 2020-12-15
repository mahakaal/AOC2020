input = [12, 1, 16, 3, 11, 0]


def get_nth(input_data: list, n: int) -> int:
    # turns start with 1
    turns: dict = {number: i for i, number in enumerate(input_data, 1)}

    # get the last number from the list
    last: int = input_data[-1]
    # cycle through all the dict, compute till n + 1
    for i in range(len(input_data), n + 1):
        # check & get the last value exists
        recent: int = turns.get(last)
        # add current index to the dict
        turns[last] = i
        # value of last is i - recent if the latter exists; 0 otherwise
        last = i - recent if recent else 0

    # it's not the last, look in the dict for the key holding value = 2020
    return list(turns.keys())[list(turns.values()).index(n)]


# part 1
print(get_nth(input, 2020))
# part 2
print(get_nth(input, 30000000))
