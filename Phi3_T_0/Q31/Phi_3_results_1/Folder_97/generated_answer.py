def if_perfect_num(nums):
    if len(nums) > 132:
        div_sum = sum([i for i in range(1, nums[132] // 2 + 1) if nums[132] % i == 0])
        return div_sum == nums[132]
    return False