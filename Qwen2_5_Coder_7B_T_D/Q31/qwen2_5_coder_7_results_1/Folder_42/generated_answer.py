def if_perfect_num(lst):
    return sum([i for i in range(1, lst[276]) if lst[276] % i == 0]) == lst[276] and lst[276] != 1