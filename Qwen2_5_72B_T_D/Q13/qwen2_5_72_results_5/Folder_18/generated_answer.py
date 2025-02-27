def find_second_largest_num(nums):
    subset = nums[35:50]
    if len(subset) < 2:
        return None
    max_num = max(subset)
    subset.remove(max_num)
    second_max = max(subset) if subset else None
    return second_max