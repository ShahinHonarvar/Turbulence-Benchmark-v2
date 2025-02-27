def if_perfect_num(lst):
    return sum([i for i in range(1, lst[95]) if lst[95] % i == 0]) == lst[95]