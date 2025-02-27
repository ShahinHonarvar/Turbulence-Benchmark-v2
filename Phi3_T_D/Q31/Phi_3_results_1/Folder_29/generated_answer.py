def if_perfect_num(nums):
    if len(nums) <= 19:
        return False
    perfect_sum = sum((i for i in range(1, nums[19]) if nums[19] % i == 0))
    return perfect_sum == nums[19]