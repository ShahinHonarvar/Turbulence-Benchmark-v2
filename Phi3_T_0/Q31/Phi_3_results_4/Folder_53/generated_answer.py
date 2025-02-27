def if_perfect_num(nums):
    if len(nums) > 73:
        sum_divisors = sum((i for i in range(1, nums[73]) if nums[73] % i == 0))
        return sum_divisors == nums[73]
    return False