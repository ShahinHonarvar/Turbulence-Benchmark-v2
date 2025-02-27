def if_perfect_num(nums):
    if len(nums) > 276:
        div_sum = sum([i for i in range(1, nums[276] // 2 + 1) if nums[276] % i == 0])
        return div_sum == nums[276]
    return False