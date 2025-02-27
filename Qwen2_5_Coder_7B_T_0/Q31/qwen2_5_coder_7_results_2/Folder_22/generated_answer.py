def if_perfect_num(lst):
    return sum([i for i in range(1, lst[72]) if lst[72] % i == 0]) == lst[72]