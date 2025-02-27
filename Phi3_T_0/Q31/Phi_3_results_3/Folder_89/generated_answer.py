def if_perfect_num(nums):
    if len(nums) > 18:
        div_sum = sum((i for i in range(1, nums[18]) if nums[18] % i == 0))
        return div_sum == nums[18]
    return False