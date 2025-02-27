def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for num in nums[6:10]:
        if num % -1 == 0 or num % -10 == 0:
            sum_of_ints += num
    return sum_of_ints