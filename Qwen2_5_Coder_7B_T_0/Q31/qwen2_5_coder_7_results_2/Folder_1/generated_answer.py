def if_perfect_num(lst):
    return sum([i for i in range(1, lst[85]) if lst[85] % i == 0]) == lst[85]