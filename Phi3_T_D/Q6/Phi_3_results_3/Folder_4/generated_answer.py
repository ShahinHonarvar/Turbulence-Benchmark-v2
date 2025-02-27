def all_neg_ints_exclusive(nums):
    return [num for i, num in enumerate(nums[10:76], start=10) if num < 0]