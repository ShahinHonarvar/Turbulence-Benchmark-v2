def if_perfect_num(nums):
    if len(nums) > 91:
        sum_of_divisors = sum((i for i in range(1, nums[91]) if nums[91] % i == 0))
        return sum_of_divisors == nums[91]
    return False