def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if i >= 80 and i <= 200 and (num % 10 == 0) and (num % 1000 == 0)]