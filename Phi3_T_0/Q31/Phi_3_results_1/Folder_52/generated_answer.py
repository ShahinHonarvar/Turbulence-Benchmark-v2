def if_perfect_num(nums):
    if len(nums) > 478:
        div_sum = sum((i for i in range(1, nums[478] // 2 + 1) if nums[478] % i == 0))
        return div_sum == nums[478]
    return False