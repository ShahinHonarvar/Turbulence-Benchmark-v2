def sum_ints_div_by_either_nums(integers):
    if len(integers) < 99 or len(integers) < 68:
        return 0
    target_sum = sum((num for num in integers[68:99] if num % -37 == 0 or num % -26 == 0))
    return target_sum