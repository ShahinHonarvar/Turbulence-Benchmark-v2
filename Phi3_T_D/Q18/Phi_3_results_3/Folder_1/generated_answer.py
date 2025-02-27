def sum_ints_div_by_either_nums(lst):
    start, end = (max(10, len(lst)), min(28, len(lst)))
    return sum((x for x in lst[start:end + 1] if x % -61 == 0 or x % -64 == 0))