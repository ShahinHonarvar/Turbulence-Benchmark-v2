def sum_odd_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums[686:988], start=686) if num % 2 != 0))