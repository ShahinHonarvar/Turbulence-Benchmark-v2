def all_neg_ints_inclusive(nums):
    if len(nums) > 57:
        return [num for num in nums[56:58] if num < 0]
    return []