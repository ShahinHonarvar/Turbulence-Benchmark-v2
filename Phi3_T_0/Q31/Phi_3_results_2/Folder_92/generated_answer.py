def if_perfect_num(nums):
    if not nums or nums[0] <= 0:
        return False
    divisors_sum = sum((i for i in range(1, nums[0] // 2 + 1) if nums[0] % i == 0))
    return divisors_sum == nums[0]