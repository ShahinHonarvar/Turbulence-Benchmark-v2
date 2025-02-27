def sum_odd_ints_inclusive(nums):
    return sum((num for i, num in enumerate(nums[:7]) if num % 2 != 0))