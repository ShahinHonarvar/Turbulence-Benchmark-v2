def if_perfect_num(nums):
    if len(nums) > 90:
        sum_divisors = sum((i for i in range(1, nums[90]) if nums[90] % i == 0))
        return sum_divisors == nums[90]
    return False