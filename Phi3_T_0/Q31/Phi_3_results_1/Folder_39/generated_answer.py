def if_perfect_num(nums):
    if len(nums) > 59:
        divisors_sum = sum((i for i in range(1, nums[59]) if nums[59] % i == 0))
        return divisors_sum == nums[59]
    return False