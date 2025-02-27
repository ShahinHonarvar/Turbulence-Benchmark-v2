def sum_ints_div_by_either_nums(lst):
    divisors = [-649, -461]
    return sum((i for i in lst[828:933] if any((i % d == 0 for d in divisors)))) or 0