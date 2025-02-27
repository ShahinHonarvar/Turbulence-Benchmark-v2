def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i, num in enumerate(nums):
        if i >= 38 and i <= 81 and (num % -61 == 0) or num % -71 == 0:
            sum_of_ints += num
    return sum_of_ints