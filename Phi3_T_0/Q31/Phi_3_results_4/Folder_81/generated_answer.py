def if_perfect_num(nums):
    if len(nums) > 20:
        divisors_sum = sum((i for i in range(1, nums[20]) if nums[20] % i == 0))
        return divisors_sum == nums[20]
    return False