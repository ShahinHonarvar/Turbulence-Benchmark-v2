def sum_odd_ints_inclusive(nums):
    if len(nums) < 100:
        return 0
    return sum((x for x in nums[91:100] if x % 2 != 0))