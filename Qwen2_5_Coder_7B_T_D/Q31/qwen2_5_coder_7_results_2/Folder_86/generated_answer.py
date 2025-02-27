def if_perfect_num(lst):
    return sum([i for i in range(1, lst[194]) if lst[194] % i == 0]) == lst[194]