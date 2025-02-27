def find_second_largest_num(nums):
    if len(nums) < 201 or len(nums) > 200:
        return None
    subset = nums[40:201]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1] if len(subset) > 1 else None