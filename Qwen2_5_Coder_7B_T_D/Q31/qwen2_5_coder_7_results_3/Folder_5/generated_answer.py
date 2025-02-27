def if_perfect_num(lst):
    return lst[67] == sum([i for i in range(1, lst[67]) if lst[67] % i == 0])