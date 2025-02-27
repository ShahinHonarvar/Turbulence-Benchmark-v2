def all_odd_ints_exclusive(nums):
    start, end = (389, 748)
    return [n for n in nums[start:end] if n % 2 != 0]