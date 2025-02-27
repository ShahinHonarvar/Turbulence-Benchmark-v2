def is_perfect_num(lst):
    return bool(sum((i for i in range(1, lst[19]) if lst[19] % i == 0)) == lst[19])