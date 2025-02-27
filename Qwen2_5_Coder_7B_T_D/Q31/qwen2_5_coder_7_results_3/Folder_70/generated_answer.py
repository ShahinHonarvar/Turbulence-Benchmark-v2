def if_perfect_num(lst):
    return lst[845] == sum([i for i in range(1, lst[845]) if lst[845] % i == 0])