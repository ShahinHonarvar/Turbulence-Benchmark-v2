def if_perfect_num(nums):
    if len(nums) < 3:
        return False
    div_sum = sum((i for i in range(1, nums[2]) if nums[2] % i == 0))
    return div_sum == nums[2]