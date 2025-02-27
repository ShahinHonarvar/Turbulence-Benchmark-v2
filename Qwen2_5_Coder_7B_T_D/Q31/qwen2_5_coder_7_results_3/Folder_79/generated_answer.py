def if_perfect_num(lst):
    return sum([i for i in range(1, 63) if 63 % i == 0]) == 63