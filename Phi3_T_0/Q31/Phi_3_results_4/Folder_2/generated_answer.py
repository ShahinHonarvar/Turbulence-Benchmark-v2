def if_perfect_num(nums):
    if len(nums) > 702:
        div_sum = sum((i for i in range(1, nums[702]) if nums[702] % i == 0))
        return div_sum == nums[702]
    return False