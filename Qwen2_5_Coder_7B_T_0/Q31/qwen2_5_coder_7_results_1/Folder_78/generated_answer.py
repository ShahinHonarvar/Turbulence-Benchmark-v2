def if_perfect_num(lst):
    return sum([i for i in range(1, lst[91]) if lst[91] % i == 0]) == lst[91]