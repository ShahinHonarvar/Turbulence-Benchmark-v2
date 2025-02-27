def all_neg_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 26 and i <= 52 and (num < 0)]