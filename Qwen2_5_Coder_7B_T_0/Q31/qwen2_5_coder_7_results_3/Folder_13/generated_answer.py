def if_perfect_num(lst):
    return sum([i for i in range(1, lst[126]) if lst[126] % i == 0]) == lst[126]