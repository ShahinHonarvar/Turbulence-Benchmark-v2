def sum_odd_ints_inclusive(nums):
    return sum((num for num in nums[20:201] if num % 2 != 0))