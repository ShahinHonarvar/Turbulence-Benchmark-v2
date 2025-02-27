def find_second_largest_num(nums):
    if len(nums) < 201:
        return None
    subset = nums[200:201]
    if len(subset) < 2:
        return None
    return sorted(subset)[-2]