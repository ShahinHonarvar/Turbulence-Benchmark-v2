def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for i, num in enumerate(nums):
        if i >= 281 and i <= 694 and (num % -722 == 0 or num % -731 == 0):
            sum_of_ints += num
    return sum_of_ints