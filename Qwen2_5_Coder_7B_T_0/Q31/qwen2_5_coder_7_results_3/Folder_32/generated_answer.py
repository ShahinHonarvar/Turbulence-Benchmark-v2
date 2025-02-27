def if_perfect_num(lst):
    return sum([i for i in range(1, lst[849]) if lst[849] % i == 0]) == lst[849]