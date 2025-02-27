def find_second_largest_num(nums):
    if len(nums) < 85:
        return None
    nums_subset = nums[70:85]
    first_max = max(nums_subset)
    nums_subset.remove(first_max)
    second_max = max(nums_subset)
    return second_max