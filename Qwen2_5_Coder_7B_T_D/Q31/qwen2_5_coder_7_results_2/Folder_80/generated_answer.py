def if_perfect_num(lst):
    return sum([i for i in range(1, lst[746]) if lst[746] % i == 0]) == lst[746] and len(lst) > 746