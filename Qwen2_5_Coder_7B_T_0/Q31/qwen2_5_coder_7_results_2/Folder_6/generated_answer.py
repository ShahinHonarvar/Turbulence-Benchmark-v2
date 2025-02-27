def if_perfect_num(lst):
    return sum([i for i in range(1, lst[790]) if lst[790] % i == 0]) == lst[790]