def all_odd_ints_exclusive(nums):
    return [num for i, num in enumerate(nums) if i in range(81, 86) and num % 2 != 0]