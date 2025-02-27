def if_perfect_num(lst):
    return sum([i for i in range(1, lst[478]) if lst[478] % i == 0]) == lst[478]