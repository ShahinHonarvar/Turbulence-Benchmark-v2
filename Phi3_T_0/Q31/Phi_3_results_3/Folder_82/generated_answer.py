def if_perfect_num(nums):
    if len(nums) > 83:
        sum_divisors = sum((i for i in range(1, nums[83]) if nums[83] % i == 0))
        return sum_divisors == nums[83]
    return False