def checkio(num):
    multi = 1
    for char in str(num).replace('0', ''):
        multi *= int(char)
    return multi


assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1