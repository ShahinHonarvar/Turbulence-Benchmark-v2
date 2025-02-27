def sum_odd_ints_inclusive(nums):
    total = sum((num for num in nums[42:52] if num % 2 != 0))
    return total