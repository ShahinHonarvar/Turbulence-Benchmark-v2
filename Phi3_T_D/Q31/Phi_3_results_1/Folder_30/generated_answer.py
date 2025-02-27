def if_perfect_num(lst):
    if len(lst) > 94:
        return sum([i for i in range(1, lst[94]) if lst[94] % i == 0]) == lst[94]
    return False