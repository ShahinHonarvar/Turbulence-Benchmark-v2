def all_neg_ints_exclusive(nums):
    return [x for i, x in enumerate(nums) if 10 < i < 76 and x < 0]