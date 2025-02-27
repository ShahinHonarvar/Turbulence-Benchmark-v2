def all_ints_div_by_both_two_nums(lst):
    divisor_product = 982 * 319
    target_range = lst[306:958]
    divisible_ints = [num for num in target_range if num % divisor_product == 0]
    return divisible_ints