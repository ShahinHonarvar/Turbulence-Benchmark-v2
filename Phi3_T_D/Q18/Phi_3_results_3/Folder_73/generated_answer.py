def sum_ints_div_by_either_nums(lst):
    start_idx, end_idx = (81, 86)
    sum_result = sum((n for i, n in enumerate(lst[start_idx:end_idx + 1], start_idx) if n % -33 == 0 or n % -62 == 0))
    return sum_result