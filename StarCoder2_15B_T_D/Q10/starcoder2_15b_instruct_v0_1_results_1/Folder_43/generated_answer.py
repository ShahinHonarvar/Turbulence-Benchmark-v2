def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 38 and i < 77 and (num % 2 == 1)]