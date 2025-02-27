def if_perfect_num(lst):
    return sum([i for i in range(1, lst[41]) if lst[41] % i == 0]) == lst[41]