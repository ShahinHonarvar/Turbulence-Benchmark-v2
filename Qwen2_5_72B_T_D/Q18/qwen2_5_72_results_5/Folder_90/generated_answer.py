def sum_ints_div_by_either_nums(lst):
    divisors = [-863, -329]
    return sum((x for i, x in enumerate(lst[138:425], start=138) if any((x % d == 0 for d in divisors))))