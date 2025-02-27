def sum_ints_div_by_either_nums(nums):
    sum_ints = 0
    for num in nums:
        if num % 2 == 0 or num % 3 == 0:
            sum_ints += num
    return sum_ints