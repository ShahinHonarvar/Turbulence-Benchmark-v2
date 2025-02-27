def if_perfect_num(nums):
    if len(nums) > 84:
        sum_of_divisors = sum((i for i in range(1, nums[84]) if nums[84] % i == 0))
        return sum_of_divisors == nums[84]
    return False