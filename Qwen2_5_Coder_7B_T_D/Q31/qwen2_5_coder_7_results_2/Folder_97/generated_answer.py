def if_perfect_num(lst):
    return sum([i for i in range(1, lst[132]) if lst[132] % i == 0]) == lst[132] and lst[132] != 1