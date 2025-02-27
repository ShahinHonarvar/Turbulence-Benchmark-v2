def all_ints_div_by_both_two_nums(lst):
    start_index, end_index = (35, 64)
    divisors = [-30, -95]
    return [x for x in lst[start_index:end_index + 1] if all((x % d == 0 for d in divisors))]