def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if i >= 154 and i <= 798 and (num % 275 == 0) and (num % 580 == 0)]