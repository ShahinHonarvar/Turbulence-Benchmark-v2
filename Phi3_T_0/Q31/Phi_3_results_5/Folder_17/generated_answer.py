def if_perfect_num(nums):
    if len(nums) > 632:
        div_sum = sum((i for i in range(1, nums[632]) if nums[632] % i == 0))
        return div_sum == nums[632]
    return False