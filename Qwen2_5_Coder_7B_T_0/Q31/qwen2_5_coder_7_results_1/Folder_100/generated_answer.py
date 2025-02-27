def if_perfect_num(lst):
    return sum([i for i in range(1, lst[99]) if lst[99] % i == 0]) == lst[99]