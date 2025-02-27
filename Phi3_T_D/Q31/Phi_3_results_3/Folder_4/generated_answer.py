def if_perfect_num(lst):
    return sum((i for i in range(1, 16) if lst[15] % i == 0)) == 2 * lst[15]