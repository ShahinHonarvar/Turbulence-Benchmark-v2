def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if 11 <= i < 76 and num % 2 == 1]