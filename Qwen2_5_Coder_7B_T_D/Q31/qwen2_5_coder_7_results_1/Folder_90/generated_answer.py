def if_perfect_num(lst):
    return lst[263] == sum((i for i in range(1, lst[263]) if lst[263] % i == 0))