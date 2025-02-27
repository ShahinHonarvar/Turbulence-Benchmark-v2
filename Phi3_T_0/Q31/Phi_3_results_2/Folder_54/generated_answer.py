def if_perfect_num(nums):
    if len(nums) > 51:
        divisors_sum = sum((i for i in range(1, nums[51]) if nums[51] % i == 0))
        return divisors_sum == nums[51]
    return False