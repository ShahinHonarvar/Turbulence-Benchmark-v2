def if_perfect_num(nums):
    if len(nums) < 4:
        return False
    div_sum = sum((i for i in range(1, nums[3]) if nums[3] % i == 0))
    return div_sum == nums[3]