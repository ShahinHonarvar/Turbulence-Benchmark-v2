def all_neg_ints_exclusive(nums):
    return [num for num in nums[5:] + nums[:4] if num < 0]