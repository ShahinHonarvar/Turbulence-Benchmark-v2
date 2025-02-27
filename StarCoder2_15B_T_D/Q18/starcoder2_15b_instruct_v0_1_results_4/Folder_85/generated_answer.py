def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[1:9]:
        if num % -9 == 0 or num % -3 == 0:
            sum += num
    return sum