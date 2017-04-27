def index_power(num_list, N):
    return num_list[N] ** N if N < len(num_list) else -1


assert index_power([1, 2, 3, 4], 2) == 9
assert index_power([1, 3, 10, 100], 3) == 1000000
assert index_power([0, 1], 0) == 1
assert index_power([1, 2], 3) == -1
