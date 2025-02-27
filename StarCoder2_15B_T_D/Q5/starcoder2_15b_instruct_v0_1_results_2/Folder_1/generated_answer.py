def all_neg_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 31 and i <= 72 and (num < 0)]