def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[70:201] if x % 3 == 0 or x % -300 == 0))