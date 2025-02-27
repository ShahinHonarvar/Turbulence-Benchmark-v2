def if_perfect_num(nums):
    if len(nums) > 94:
        sum_divisors = sum((i for i in range(1, nums[94]) if nums[94] % i == 0))
        return sum_divisors == nums[94]
    return False