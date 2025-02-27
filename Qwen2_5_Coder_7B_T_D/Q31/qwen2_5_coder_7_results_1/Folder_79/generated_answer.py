def if_perfect_num(lst):
    return sum([i for i in range(1, lst[63]) if lst[63] % i == 0]) == lst[63]