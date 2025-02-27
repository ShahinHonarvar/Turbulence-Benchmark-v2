def if_perfect_num(nums):
    if len(nums) > 66:
        sum_divisors = sum((i for i in range(1, nums[66]) if nums[66] % i == 0))
        return sum_divisors == nums[66]
    return False