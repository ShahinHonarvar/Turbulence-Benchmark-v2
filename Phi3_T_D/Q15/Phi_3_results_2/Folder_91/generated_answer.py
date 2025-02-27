def sum_odd_ints_inclusive(integers):
    return sum(filter(lambda x: x % 2 != 0, integers[:6]))