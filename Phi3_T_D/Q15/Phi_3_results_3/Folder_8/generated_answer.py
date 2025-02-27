def sum_odd_ints_inclusive(nums):
    start, end = (23, 23)
    odd_sum = sum((num for num in nums[start:end + 1] if num % 2 != 0))
    return odd_sum