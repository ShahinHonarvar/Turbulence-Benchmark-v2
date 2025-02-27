def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[299:383]) if num % 858 == 0 or num % 952 == 0))