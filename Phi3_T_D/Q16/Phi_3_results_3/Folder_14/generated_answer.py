def sum_even_ints_inclusive(nums):
    start, end = (5, 7)
    return sum((num for num in nums[start:end + 1] if num % 2 == 0))