def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if num % -201 != 0 and 495 < i < 826]