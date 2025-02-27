def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if 20 < i < 200 and num % 2 != 0]