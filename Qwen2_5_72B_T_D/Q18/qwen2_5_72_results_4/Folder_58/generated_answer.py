def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[240:902], start=240) if num % 546 == 0 or num % 709 == 0))