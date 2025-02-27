def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 5 and i <= 7 and (num % 2 == 1)]