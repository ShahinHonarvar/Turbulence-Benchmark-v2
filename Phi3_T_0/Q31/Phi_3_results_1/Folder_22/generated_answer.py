def if_perfect_num(nums):
    if len(nums) > 72:
        sum_divisors = sum((i for i in range(1, nums[72]) if nums[72] % i == 0))
        return sum_divisors == nums[72]
    return False