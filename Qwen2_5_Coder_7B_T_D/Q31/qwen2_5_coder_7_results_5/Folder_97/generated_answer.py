def if_perfect_num(lst):
    return lst[132] == sum((i for i in range(1, lst[132]) if lst[132] % i == 0))