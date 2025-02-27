def all_even_ints_inclusive(nums):
    start, end = (29, 93)
    return [num for num in nums[start:end + 1] if num % 2 == 0]