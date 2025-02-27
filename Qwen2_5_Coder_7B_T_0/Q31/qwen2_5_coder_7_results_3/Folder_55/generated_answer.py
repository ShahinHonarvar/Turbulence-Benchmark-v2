def if_perfect_num(lst):
    return sum([i for i in range(1, lst[21]) if lst[21] % i == 0]) == lst[21]