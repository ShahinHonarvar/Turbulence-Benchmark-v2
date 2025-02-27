def if_perfect_num(lst):
    return sum([i for i in range(1, lst[28]) if lst[28] % i == 0]) == lst[28]