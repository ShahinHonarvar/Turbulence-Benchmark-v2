def sum_ints_div_by_either_nums(lst):
    divisors = [-649, -461]
    return sum((x for i, x in enumerate(lst[828:933]) if any((x % d == 0 for d in divisors))))