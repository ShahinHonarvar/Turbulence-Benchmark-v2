def if_perfect_num(lst):
    return sum([i for i in range(1, lst[38]) if lst[38] % i == 0]) == lst[38]