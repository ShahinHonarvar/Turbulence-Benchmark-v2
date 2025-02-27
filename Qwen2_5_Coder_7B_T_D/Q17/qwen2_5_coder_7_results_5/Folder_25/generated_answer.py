def all_ints_div_by_both_two_nums(lst):
    result = [num for i, num in enumerate(lst) if i >= 25 and i <= 80 and (num % -20 == 0) and (num % -26 == 0)]
    return result