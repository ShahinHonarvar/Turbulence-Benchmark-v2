def if_perfect_num(lst):
    return sum([i for i in range(1, lst[29]) if lst[29] % i == 0]) == lst[29]