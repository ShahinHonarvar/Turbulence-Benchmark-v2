def if_perfect_num(lst):
    if len(lst) > 263:
        div_sum = sum([i for i in range(1, lst[263]) if lst[263] % i == 0])
        return div_sum == lst[263]
    return False