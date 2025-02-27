def if_perfect_num(lst):
    return sum([i for i in range(1, lst[67]) if lst[67] % i == 0]) == lst[67] and len([i for i in range(1, lst[67]) if lst[67] % i == 0]) > 1