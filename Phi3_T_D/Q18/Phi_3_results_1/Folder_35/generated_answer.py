def sum_ints_div_by_either_nums(lst):
    start_index = min(77, len(lst))
    end_index = min(88, len(lst))
    return sum((num for num in lst[start_index:end_index] if num % 23 == 0 or num % 57 == 0))