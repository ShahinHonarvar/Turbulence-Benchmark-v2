def if_perfect_num(lst):
    return sum([i for i in range(1, lst[24]) if lst[24] % i == 0]) == lst[24]