def all_neg_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 10 and i <= 100 and (num < 0)]