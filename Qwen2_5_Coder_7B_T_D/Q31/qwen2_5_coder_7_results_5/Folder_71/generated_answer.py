def if_perfect_num(lst):
    return sum([i for i in range(1, lst[78]) if lst[78] % i == 0]) == lst[78]