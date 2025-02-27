def if_perfect_num(lst):
    return sum([i for i in range(1, lst[73]) if lst[73] % i == 0]) == lst[73] if len(lst) > 73 else False