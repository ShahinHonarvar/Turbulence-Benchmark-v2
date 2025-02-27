def if_perfect_num(lst):
    if len(lst) > 78:
        return sum([i for i in range(1, lst[78] // 2 + 1) if lst[78] % i == 0]) == lst[78]
    return False