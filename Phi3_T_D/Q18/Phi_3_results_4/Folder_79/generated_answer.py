def sum_ints_div_by_either_nums(lst):
    start, end = (8, 9)
    return sum((x for x in lst[start:end + 1] if x % -3 == 0 or x % 6 == 0))