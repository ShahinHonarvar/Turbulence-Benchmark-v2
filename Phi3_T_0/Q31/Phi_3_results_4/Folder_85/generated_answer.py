def if_perfect_num(nums):
    if len(nums) > 23:
        div_sum = sum((i for i in range(1, nums[23]) if nums[23] % i == 0))
        return div_sum == nums[23]
    return False