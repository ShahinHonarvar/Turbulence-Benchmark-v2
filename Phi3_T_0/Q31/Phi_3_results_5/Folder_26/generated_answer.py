def if_perfect_num(nums):
    if len(nums) > 222:
        div_sum = sum([i for i in range(1, nums[222] // 2 + 1) if nums[222] % i == 0])
        return div_sum == nums[222]
    return False