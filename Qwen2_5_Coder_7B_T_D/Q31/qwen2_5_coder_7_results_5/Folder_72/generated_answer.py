def if_perfect_num(lst):
    return sum([i for i in range(1, lst[16]) if lst[16] % i == 0]) == lst[16] and len(lst) > 16