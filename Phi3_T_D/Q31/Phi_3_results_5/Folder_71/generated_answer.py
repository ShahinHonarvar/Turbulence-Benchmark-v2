def if_perfect_num(nums):
    if len(nums) > 78:
        sum_of_divisors = sum((i for i in range(1, nums[78]) if nums[78] % i == 0))
        return sum_of_divisors == nums[78]
    return False