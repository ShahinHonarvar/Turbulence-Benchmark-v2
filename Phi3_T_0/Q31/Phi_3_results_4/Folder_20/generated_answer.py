def if_perfect_num(nums):
    if len(nums) > 53:
        divisors_sum = sum((i for i in range(1, nums[53]) if nums[53] % i == 0))
        return divisors_sum == nums[53]
    return False