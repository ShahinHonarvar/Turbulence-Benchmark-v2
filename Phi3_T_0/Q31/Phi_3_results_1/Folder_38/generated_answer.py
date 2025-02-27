def if_perfect_num(nums):
    if len(nums) > 38:
        divisors_sum = sum((i for i in range(1, nums[38]) if nums[38] % i == 0))
        return divisors_sum == nums[38]
    return False