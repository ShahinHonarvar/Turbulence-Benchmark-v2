def if_perfect_num(nums):
    if len(nums) > 733:
        div_sum = sum([i for i in range(1, nums[733] // 2 + 1) if nums[733] % i == 0])
        return div_sum == nums[733]
    return False