def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i in range(36, 54) and num % 2 == 1]