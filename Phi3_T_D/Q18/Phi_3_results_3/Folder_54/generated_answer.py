def sum_ints_div_by_either_nums(lst):
    sum_divisible = sum((num for num in lst[13:92] if num % -65 == 0 or num % -62 == 0))
    return sum_divisible