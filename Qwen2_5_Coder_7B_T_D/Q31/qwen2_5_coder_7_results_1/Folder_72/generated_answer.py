def if_perfect_num(lst):
    return lst[16] == sum([i for i in range(1, lst[16]) if lst[16] % i == 0])