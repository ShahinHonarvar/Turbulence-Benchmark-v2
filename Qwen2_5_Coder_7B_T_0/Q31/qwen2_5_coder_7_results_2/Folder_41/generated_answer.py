def if_perfect_num(lst):
    return sum([i for i in range(1, lst[84]) if lst[84] % i == 0]) == lst[84]