def if_perfect_num(lst):
    return sum([i for i in range(1, lst[410]) if lst[410] % i == 0]) == lst[410]