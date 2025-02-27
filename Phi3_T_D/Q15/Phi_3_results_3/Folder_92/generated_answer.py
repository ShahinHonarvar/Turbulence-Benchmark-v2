def sum_odd_ints_inclusive(nums):
    return sum((i for i in nums[1:2] if i % 2 != 0))