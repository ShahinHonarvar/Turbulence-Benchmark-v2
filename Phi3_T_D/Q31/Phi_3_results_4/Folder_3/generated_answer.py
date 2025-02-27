def if_perfect_num(lst):
    if len(lst) > 100:
        return True if sum([i for i in range(1, lst[100]) if lst[100] % i == 0]) == lst[100] * 2 - lst[100] else False
    return False