def if_perfect_num(lst):
    return sum([i for i in range(1, lst[100]) if lst[100] % i == 0]) == lst[100]