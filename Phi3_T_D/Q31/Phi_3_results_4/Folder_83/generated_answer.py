def if_perfect_num(nums):
    if len(nums) > 95:
        div_sum = sum([i for i in range(1, nums[95]) if nums[95] % i == 0])
        return div_sum == nums[95]
    return False