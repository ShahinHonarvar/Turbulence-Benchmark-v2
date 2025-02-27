def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[299:383], start=299) if x % 858 == 0 or x % 952 == 0))