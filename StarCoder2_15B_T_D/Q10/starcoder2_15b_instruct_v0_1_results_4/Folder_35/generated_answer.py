def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if 10 <= i < 80 and num % 2 == 1]