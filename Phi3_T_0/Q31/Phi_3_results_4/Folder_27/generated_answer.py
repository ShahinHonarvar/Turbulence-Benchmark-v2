def if_perfect_num(nums):
    if len(nums) > 56:
        divisors_sum = sum((i for i in range(1, nums[56]) if nums[56] % i == 0))
        return divisors_sum == nums[56]
    return False