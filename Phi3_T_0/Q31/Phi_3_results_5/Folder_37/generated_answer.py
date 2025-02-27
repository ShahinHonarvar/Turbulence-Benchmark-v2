def if_perfect_num(nums):
    if len(nums) > 28:
        divisors_sum = sum((i for i in range(1, nums[28]) if nums[28] % i == 0))
        return divisors_sum == nums[28]
    return False