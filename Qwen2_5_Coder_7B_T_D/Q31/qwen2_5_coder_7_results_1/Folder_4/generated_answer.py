def if_perfect_num(lst):
    return sum([i for i in range(1, lst[15]) if lst[15] % i == 0]) == lst[15] and lst[15] != 1