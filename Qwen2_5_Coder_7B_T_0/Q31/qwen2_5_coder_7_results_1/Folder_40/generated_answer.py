def if_perfect_num(lst):
    return sum([i for i in range(1, lst[7]) if lst[7] % i == 0]) == lst[7] and lst[7] != 1