def if_perfect_num(lst):
    return sum([i for i in range(1, lst[162]) if lst[162] % i == 0]) == lst[162]