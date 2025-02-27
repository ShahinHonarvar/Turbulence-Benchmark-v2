def if_perfect_num(nums):
    if len(nums) > 96:
        perfect_sum = sum((i for i in range(1, nums[96]) if nums[96] % i == 0))
        return perfect_sum == nums[96]
    else:
        return False