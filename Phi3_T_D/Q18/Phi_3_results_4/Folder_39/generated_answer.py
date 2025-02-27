def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[13:77], start=13) if num % -66 == 0 or num % -32 == 0))