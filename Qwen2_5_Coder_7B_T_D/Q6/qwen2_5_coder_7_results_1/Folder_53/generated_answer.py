def all_neg_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if 100 < i < 200 and num < 0]