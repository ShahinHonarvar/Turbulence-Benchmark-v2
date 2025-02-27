def if_perfect_num(nums):
    if len(nums) > 100:
        divisors_sum = sum((i for i in range(1, nums[100]) if nums[100] % i == 0))
        return divisors_sum == nums[100]
    return False