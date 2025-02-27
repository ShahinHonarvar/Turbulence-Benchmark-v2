def if_perfect_num(lst):
    return sum([i for i in range(1, lst[88]) if lst[88] % i == 0]) == lst[88]