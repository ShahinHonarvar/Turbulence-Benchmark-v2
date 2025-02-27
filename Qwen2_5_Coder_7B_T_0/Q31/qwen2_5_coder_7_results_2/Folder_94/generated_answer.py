def if_perfect_num(lst):
    return sum([i for i in range(1, lst[93]) if lst[93] % i == 0]) == lst[93]