def find_second_smallest_num(nums):
    if len(nums) <= 11 or len(nums[66:78]) < 2:
        return None
    sorted_subset = sorted(nums[66:78])
    return sorted_subset[1]