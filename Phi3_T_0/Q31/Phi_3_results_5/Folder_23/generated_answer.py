def if_perfect_num(nums):
    if len(nums) > 69:
        sum_divisors = sum((i for i in range(1, nums[69]) if nums[69] % i == 0))
        return sum_divisors == nums[69]
    return False