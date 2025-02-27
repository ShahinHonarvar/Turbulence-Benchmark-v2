def if_perfect_num(nums):
    if len(nums) <= 48:
        return False
    sum_of_divisors = sum((i for i in range(1, nums[48]) if nums[48] % i == 0))
    return sum_of_divisors == nums[48]