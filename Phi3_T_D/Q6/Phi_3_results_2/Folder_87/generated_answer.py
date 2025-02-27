def all_neg_ints_exclusive(nums):
    start, end = (32, 99)
    return [num for i, num in enumerate(nums[start:end]) if num < 0]