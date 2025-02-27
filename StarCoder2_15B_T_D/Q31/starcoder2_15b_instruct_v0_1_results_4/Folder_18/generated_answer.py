def if_perfect_num(nums):
    divisor_sum = 0
    for i in range(1, nums[312]):
        if nums[312] % i == 0:
            divisor_sum += i
    return divisor_sum == nums[312]