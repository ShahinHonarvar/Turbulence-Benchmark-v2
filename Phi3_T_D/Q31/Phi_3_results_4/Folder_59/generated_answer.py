def if_perfect_num(lst):
    return bool(sum((i for i in range(1, lst[2] // 2 + 1) if lst[2] % i == 0)) == lst[2])