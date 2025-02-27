def if_perfect_num(nums):
    if len(nums) > 78:
        divisors_sum = sum((i for i in range(1, nums[78]) if nums[78] % i == 0))
        return divisors_sum == nums[78]
    return False