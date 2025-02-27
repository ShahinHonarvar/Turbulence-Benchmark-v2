def if_perfect_num(lst):
    return sum([i for i in range(1, lst[96]) if lst[96] % i == 0]) == lst[96]