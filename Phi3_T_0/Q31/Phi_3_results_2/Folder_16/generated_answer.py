def if_perfect_num(nums):
    if len(nums) > 162:
        div_sum = sum([i for i in range(1, nums[162] // 2 + 1) if nums[162] % i == 0])
        return div_sum == nums[162]
    return False