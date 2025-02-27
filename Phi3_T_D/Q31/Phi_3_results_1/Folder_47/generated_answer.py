def if_perfect_num(nums):
    if len(nums) <= 34:
        return False
    perfect_sum = sum((i for i in range(1, nums[34]) if nums[34] % i == 0))
    return perfect_sum == nums[34]