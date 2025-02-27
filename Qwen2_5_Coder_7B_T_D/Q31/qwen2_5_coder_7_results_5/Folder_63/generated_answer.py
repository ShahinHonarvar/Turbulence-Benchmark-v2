def if_perfect_num(lst):
    return sum([i for i in range(1, lst[57]) if lst[57] % i == 0]) == lst[57] and lst[57] != 1