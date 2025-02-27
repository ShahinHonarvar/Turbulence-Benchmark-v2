def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 361 and i < 643 and (num % 2 == 1)]