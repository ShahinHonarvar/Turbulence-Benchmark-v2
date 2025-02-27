def if_perfect_num(lst):
    return sum([i for i in range(1, lst[222]) if lst[222] % i == 0]) == lst[222]