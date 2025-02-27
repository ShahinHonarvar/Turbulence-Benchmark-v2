def if_perfect_num(nums):
    if len(nums) > 57:
        divisors_sum = sum((i for i in range(1, nums[57]) if nums[57] % i == 0))
        return divisors_sum == nums[57]
    return False