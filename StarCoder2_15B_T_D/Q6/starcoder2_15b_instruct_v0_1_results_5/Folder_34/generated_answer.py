def all_neg_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 60 and i < 200 and (num < 0)]