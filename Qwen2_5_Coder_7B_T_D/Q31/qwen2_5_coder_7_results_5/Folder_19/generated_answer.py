def if_perfect_num(lst):
    return sum([i for i in range(1, lst[13]) if lst[13] % i == 0]) == lst[13]