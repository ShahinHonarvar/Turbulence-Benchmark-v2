def if_perfect_num(nums):
    if len(nums) > 24:
        div_sum = sum((i for i in range(1, nums[24]) if nums[24] % i == 0))
        return div_sum == nums[24]
    return False