def if_perfect_num(lst):
    return sum([i for i in range(1, lst[59]) if lst[59] % i == 0]) == lst[59]