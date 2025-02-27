def sum_even_ints_inclusive(nums):
    return sum(filter(lambda x: x % 2 == 0, nums[82:87])) if len(nums) > 86 else 0