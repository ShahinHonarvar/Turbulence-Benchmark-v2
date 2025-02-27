def if_perfect_num(nums):
    if len(nums) > 247:
        div_sum = sum((i for i in range(1, nums[247]) if nums[247] % i == 0))
        return div_sum == nums[247]
    return False