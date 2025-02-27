def sum_ints_div_by_either_nums(lst):
    total_sum = sum((num for num in lst[31:51] if num % 81 == 0 or num % 64 == 0))
    return total_sum