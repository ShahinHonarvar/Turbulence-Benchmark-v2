def if_perfect_num(nums):
    if len(nums) > 51:
        div_sum = sum([i for i in range(1, nums[51] // 2 + 1) if nums[51] % i == 0])
        return div_sum == nums[51]
    else:
        return False