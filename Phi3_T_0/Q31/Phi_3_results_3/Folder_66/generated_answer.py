def if_perfect_num(nums):
    if len(nums) > 42:
        sum_divisors = sum((i for i in range(1, nums[42]) if nums[42] % i == 0))
        return sum_divisors == nums[42]
    return False