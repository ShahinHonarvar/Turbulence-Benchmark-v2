def if_perfect_num(lst):
    return sum([i for i in range(1, lst[321]) if lst[321] % i == 0]) == lst[321] if len(lst) > 321 else False