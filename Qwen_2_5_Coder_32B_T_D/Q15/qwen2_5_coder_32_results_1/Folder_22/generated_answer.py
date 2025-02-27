def sum_odd_ints_inclusive(nums):
    if len(nums) < 42:
        return 0
    return sum((x for x in nums[40:42] if x % 2 != 0))