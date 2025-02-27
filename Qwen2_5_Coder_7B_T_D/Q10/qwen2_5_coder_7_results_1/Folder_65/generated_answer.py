def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i > 42 and i < 87 and (num % 2 != 0)]