def if_perfect_num(lst):
    return sum([i for i in range(1, lst[702]) if lst[702] % i == 0]) == lst[702]