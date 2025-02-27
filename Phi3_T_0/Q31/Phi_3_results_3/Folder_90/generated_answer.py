def if_perfect_num(nums):
    if len(nums) > 263:
        div_sum = sum([i for i in range(1, nums[263] // 2 + 1) if nums[263] % i == 0])
        return div_sum == nums[263]
    return False