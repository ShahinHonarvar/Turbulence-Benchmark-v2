def all_neg_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 7 and i < 9 and (num < 0)]