def if_perfect_num(lst):
    return sum(lst[19]) == sum((i for i in range(1, lst[19]) if lst[19] % i == 0))