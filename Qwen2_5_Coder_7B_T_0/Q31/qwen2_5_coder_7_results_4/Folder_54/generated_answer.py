def if_perfect_num(lst):
    return sum([i for i in range(1, lst[51]) if lst[51] % i == 0]) == lst[51]