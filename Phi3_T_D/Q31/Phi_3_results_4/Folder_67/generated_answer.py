def if_perfect_num(nums):
    if len(nums) > 43:
        sum_of_divisors = sum((i for i in range(1, nums[43]) if nums[43] % i == 0))
        return sum_of_divisors == nums[43]
    return False