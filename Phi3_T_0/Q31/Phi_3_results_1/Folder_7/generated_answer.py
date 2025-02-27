def if_perfect_num(nums):
    if len(nums) > 851:
        div_sum = sum((i for i in range(1, nums[851]) if nums[851] % i == 0))
        return div_sum == nums[851]
    return False