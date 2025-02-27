def all_even_ints_exclusive(nums):
    return [nums[i] for i in range(100, 102) if i < len(nums) and nums[i] % 2 == 0]