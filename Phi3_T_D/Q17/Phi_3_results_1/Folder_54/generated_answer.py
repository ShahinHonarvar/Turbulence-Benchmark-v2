def all_ints_div_by_both_two_nums(lst):
    start_idx, end_idx = (13, 91)
    res = [num for num in lst[start_idx:end_idx + 1] if num % -65 == 0 and num % -62 == 0]
    return res