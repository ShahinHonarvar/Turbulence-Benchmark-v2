def all_ints_div_by_both_two_nums(numbers):
    target_indices = range(86, 90)
    divisible_nums = []
    for i in target_indices:
        if numbers[i] % -61 == 0 and numbers[i] % -79 == 0:
            divisible_nums.append(numbers[i])
    return divisible_nums