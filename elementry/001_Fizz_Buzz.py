def checkio(num):
    division_dict = {15: "Fizz Buzz", 3: "Fizz", 5: "Buzz", 1: str(num)}
    for div_num in sorted(division_dict.keys(), reverse=True):
        if num % div_num == 0:
            return division_dict[div_num]



print  checkio(15)
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(5) == "Buzz"
assert checkio(7) == "7"

# for i in xrange(1000000000):
#     if i % 15 != 0 and (i % 5 == 0 and i % 3 == 0):
#         print i