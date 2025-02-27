def if_perfect_num(nums):
    if len(nums) > 21:
        divisors_sum = sum((i for i in range(1, nums[21]) if nums[21] % i == 0))
        return divisors_sum == nums[21]
    return False