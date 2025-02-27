def all_neg_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 21 and i <= 97 and (num < 0)]