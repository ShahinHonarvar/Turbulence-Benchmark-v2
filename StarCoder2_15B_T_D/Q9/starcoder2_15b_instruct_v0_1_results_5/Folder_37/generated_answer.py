def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums) if i % 2 == 1 and 1 <= i <= 5]