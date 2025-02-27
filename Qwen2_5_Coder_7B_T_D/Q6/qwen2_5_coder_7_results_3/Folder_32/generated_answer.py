def all_neg_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i > 11 and i < 76 and (num < 0)]