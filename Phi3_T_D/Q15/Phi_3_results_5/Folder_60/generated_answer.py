def sum_odd_ints_inclusive(nums):
    return sum((n for i, n in enumerate(nums[75:86]) if n % 2 != 0))