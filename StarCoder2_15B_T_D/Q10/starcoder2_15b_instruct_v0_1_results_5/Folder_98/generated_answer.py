def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i % 2 == 1 and 0 < i < 6]