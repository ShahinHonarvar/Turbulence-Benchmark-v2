def if_perfect_num(lst):
    return lst[57] == sum([i for i in range(1, lst[57]) if lst[57] % i == 0])