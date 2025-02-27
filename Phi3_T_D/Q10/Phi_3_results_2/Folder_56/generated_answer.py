def all_odd_ints_exclusive(nums):
    start, end = (7, 9)
    return [num for num in nums[start:end] if num % 2 != 0]