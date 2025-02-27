def if_perfect_num(nums):
    factor_sum = 0
    for i in range(1, nums[18]):
        if nums[18] % i == 0:
            factor_sum += i
    return factor_sum == nums[18]