def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[32:100]:
        if num % -11 == 0 or num % -15 == 0:
            sum += num
    return sum