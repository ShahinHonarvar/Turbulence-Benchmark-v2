def if_perfect_num(lst):
    return sum([i for i in range(1, lst[247]) if lst[247] % i == 0]) == lst[247]