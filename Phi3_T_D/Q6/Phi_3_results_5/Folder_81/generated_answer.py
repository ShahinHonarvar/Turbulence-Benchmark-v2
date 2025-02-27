def all_neg_ints_exclusive(nums):
    return [n for i, n in enumerate(nums) if i > 9 and i < 99 and (n < 0)]