def all_ints_div_by_both_two_nums(lst):
    result = [num for i, num in enumerate(lst) if i >= 299 and i <= 382 and (num % 858 == 0) and (num % 952 == 0)]
    return result