def sum_ints_div_by_either_nums(lst):
    start, end = (13, 18)
    return sum((x for x in lst[start:end + 1] if x % 45 == 0 or x % 20 == 0))