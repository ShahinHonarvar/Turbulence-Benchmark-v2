def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i >= 80 and i <= 200 and (num % 2 == 1)]