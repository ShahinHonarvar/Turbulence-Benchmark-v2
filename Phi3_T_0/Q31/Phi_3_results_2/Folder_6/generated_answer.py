def if_perfect_num(nums):
    if len(nums) > 790:
        sum_divisors = sum((i for i in range(1, nums[790]) if nums[790] % i == 0))
        return sum_divisors == nums[790]
    return False