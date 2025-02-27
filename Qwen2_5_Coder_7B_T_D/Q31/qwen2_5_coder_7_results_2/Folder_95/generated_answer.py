def if_perfect_num(lst):
    return sum([i for i in range(1, lst[87]) if lst[87] % i == 0]) == lst[87] and lst[87] != 1