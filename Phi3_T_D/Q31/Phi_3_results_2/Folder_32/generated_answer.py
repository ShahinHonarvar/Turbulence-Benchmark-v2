def if_perfect_num(nums):
    if len(nums) > 849:
        sum_positive_divisors = sum((x for x in range(1, nums[849] // 2 + 1) if nums[849] % x == 0))
        return sum_positive_divisors == nums[849]
    return False