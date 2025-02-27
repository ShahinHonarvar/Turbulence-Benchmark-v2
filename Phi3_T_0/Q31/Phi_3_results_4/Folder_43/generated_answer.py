def if_perfect_num(nums):
    if len(nums) > 29:
        divisors_sum = sum((i for i in range(1, nums[29]) if nums[29] % i == 0))
        return divisors_sum == nums[29]
    return False