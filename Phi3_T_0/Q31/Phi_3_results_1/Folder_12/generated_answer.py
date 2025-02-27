def if_perfect_num(nums):
    if len(nums) > 27:
        divisors_sum = sum((i for i in range(1, nums[27]) if nums[27] % i == 0))
        return divisors_sum == nums[27]
    return False