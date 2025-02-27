def all_odd_ints_inclusive(nums):
    return [num for idx, num in enumerate(nums) if idx >= 8 and idx <= 9 and (num % 2 == 1)]