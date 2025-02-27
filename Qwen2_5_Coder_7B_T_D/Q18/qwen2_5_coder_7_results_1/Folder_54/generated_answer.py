def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst[13:92]) if num % -65 == 0 or num % -62 == 0))