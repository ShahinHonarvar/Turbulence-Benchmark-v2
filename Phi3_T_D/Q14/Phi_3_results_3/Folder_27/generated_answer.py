def find_second_smallest_num(nums):
    if len(nums) < 35 or len(nums) > 84:
        return None
    subset = nums[25:60]
    subset.sort()
    return None if len(subset) < 2 else subset[1]