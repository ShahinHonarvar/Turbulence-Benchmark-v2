def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for num in nums[31:51]:
        if num % 81 == 0 or num % 64 == 0:
            sum_of_ints += num
    return sum_of_ints