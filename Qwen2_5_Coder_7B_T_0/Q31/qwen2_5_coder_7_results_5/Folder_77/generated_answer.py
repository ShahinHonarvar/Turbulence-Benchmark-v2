def if_perfect_num(lst):
    return sum([i for i in range(1, lst[985]) if lst[985] % i == 0]) == lst[985]