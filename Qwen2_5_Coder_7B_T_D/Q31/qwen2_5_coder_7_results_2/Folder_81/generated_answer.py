def if_perfect_num(lst):
    return sum([i for i in range(1, lst[20]) if lst[20] % i == 0]) == lst[20] and lst[20] != 1