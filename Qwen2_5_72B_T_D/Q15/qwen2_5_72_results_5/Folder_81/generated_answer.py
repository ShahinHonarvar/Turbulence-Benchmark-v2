def sum_odd_ints_inclusive(nums):
    return sum((num for num in nums[10:101] if num % 2 != 0))