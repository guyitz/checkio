def checkio(int_list):
    return sum([num for i, num in enumerate(int_list) if i % 2 == 0]) * int_list[-1] if int_list else 0


assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0
