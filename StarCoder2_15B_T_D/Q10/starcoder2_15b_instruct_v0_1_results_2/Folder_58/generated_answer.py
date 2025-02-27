def all_odd_ints_exclusive(nums):
    return [num for idx, num in enumerate(nums) if idx >= 276 and idx < 376 and (num % 2 != 0)]