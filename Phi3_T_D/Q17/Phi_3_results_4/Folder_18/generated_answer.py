def all_ints_div_by_both_two_nums(integers):
    target_range = integers[55:67]
    divisible_by_both = [num for num in target_range if num % 22 == 0 and num % 82 == 0]
    return divisible_by_both