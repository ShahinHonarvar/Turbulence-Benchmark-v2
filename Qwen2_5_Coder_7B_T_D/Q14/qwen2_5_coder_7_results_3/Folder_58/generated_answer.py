def find_second_smallest_num(nums):
    if len(nums) < 371:
        return None
    subset = nums[310:371]
    if len(subset) < 2:
        return None
    subset.remove(min(subset))
    return min(subset)