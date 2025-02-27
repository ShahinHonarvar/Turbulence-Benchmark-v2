def if_perfect_num(nums):
    if len(nums) > 35:
        divisors_sum = sum((i for i in range(1, nums[35]) if nums[35] % i == 0))
        return divisors_sum == nums[35]
    return False