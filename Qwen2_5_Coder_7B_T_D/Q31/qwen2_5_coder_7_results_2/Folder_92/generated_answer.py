def if_perfect_num(lst):
    return sum([i for i in range(1, lst[0]) if lst[0] % i == 0]) == lst[0]