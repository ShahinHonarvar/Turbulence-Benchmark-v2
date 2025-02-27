def if_perfect_num(lst):
    if len(lst) > 57:
        sum_divisors = sum((i for i in range(1, lst[57]) if lst[57] % i == 0))
        return sum_divisors == lst[57]
    return False