def sum_odd_ints_inclusive(nums):
    start, end = (37, 51)
    return sum((num for num in nums[start:end + 1] if num % 2 != 0))