def if_perfect_num(lst):
    return sum([i for i in range(1, lst[56]) if lst[56] % i == 0]) == lst[56]