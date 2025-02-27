def sum_ints_div_by_either_nums(lst):
    total_sum = sum((x for i, x in enumerate(lst[240:902]) if x % 546 == 0 or x % 709 == 0))
    return total_sum