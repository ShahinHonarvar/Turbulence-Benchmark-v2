def sum_ints_div_by_either_nums(lst):
    start, end = (138, 424)
    return sum((x for x in lst[start:end + 1] if x % -863 == 0 or x % -329 == 0))