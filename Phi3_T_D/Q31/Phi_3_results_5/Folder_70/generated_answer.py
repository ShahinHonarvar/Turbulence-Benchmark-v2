def if_perfect_num(nums):
    if len(nums) > 845:
        div_sum = sum([i for i in range(1, nums[845] // 2 + 1) if nums[845] % i == 0])
        return div_sum == nums[845]
    else:
        return False