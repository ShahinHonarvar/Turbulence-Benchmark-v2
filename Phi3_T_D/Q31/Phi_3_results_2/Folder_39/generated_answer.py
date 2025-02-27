def if_perfect_num(lst):
    if len(lst) > 59:
        div_sum = sum([i for i in range(1, lst[59]) if lst[59] % i == 0])
        return div_sum == lst[59]
    return False