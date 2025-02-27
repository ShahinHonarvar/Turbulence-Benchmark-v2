def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if i >= 20 and i <= 35 and (num % -36 == 0) and (num % -89 == 0)]