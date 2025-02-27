def if_perfect_num(lst):
    return sum([i for i in range(1, lst[66]) if lst[66] % i == 0]) == lst[66] if len(lst) > 66 else False