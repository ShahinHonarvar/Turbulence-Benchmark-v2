def if_perfect_num(lst):
    return lst[28] == sum([i for i in range(1, lst[28]) if lst[28] % i == 0])