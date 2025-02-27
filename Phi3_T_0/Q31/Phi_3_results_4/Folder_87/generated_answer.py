def if_perfect_num(nums):
    if len(nums) > 96:
        sum_of_divisors = sum((i for i in range(1, nums[96]) if nums[96] % i == 0))
        return sum_of_divisors == nums[96]
    return False