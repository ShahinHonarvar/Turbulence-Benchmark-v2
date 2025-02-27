def if_perfect_num(lst):
    return sum([i for i in range(1, lst[17]) if lst[17] % i == 0]) == lst[17]