def all_ints_div_by_both_two_nums(lst):
    start, end = (81, 86)
    divisor1, divisor2 = (-33, -62)
    subset = lst[start:end + 1]
    result = [val for val in subset if val % divisor1 == 0 and val % divisor2 == 0]
    return result