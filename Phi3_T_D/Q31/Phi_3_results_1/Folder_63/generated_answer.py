def if_perfect_num(lst):
    if len(lst) > 57:
        div_sum = sum([i for i in range(1, lst[57] // 2 + 1) if lst[57] % i == 0])
        return div_sum == lst[57]
    return False