def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[70:201], start=70) if x % 3 == 0 or x % -300 == 0))