def if_perfect_num(lst):
    return sum([i for i in range(1, lst[851]) if lst[851] % i == 0]) == lst[851]