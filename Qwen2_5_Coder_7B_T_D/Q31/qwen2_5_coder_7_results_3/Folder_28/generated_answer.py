def if_perfect_num(lst):
    return sum(lst[37]) == sum([i for i in range(1, lst[37]) if lst[37] % i == 0])