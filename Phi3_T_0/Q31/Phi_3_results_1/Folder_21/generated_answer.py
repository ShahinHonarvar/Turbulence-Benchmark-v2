def if_perfect_num(nums):
    if len(nums) > 410:
        div_sum = sum((i for i in range(1, nums[410]) if nums[410] % i == 0))
        return div_sum == nums[410]
    return False