def if_perfect_num(nums):
    if len(nums) > 29:
        sum_divisors = sum((i for i in range(1, nums[29]) if nums[29] % i == 0))
        return sum_divisors == nums[29]
    return False