def if_perfect_num(nums):
    if len(nums) > 59:
        sum_divisors = sum((i for i in range(1, nums[59]) if nums[59] % i == 0))
        return sum_divisors == nums[59]
    return False