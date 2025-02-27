def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i > 6 and i < 9 and (num % 2 == 1)]