def if_perfect_num(lst):
    return lst[68] == sum((i for i in range(1, lst[68]) if lst[68] % i == 0))