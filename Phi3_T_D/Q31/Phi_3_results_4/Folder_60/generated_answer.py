def is_perfect_num(nums):
    if len(nums) > 88:
        divisor_sum = sum([i for i in range(1, nums[88] // 2 + 1) if nums[88] % i == 0])
        return divisor_sum == nums[88]
    return False