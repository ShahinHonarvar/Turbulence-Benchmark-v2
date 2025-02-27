def all_neg_ints_exclusive(nums):
    return [n for i, n in enumerate(nums) if i > 0 and i < 9 and (n < 0)]