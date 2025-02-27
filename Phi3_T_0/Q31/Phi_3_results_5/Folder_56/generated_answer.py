def if_perfect_num(nums):
    if len(nums) > 60:
        div_sum = sum((i for i in range(1, nums[60]) if nums[60] % i == 0))
        return div_sum == nums[60]
    return False