def find_second_largest_num(nums):
    if len(nums[30:201]) < 2:
        return None
    return sorted(set(nums[30:201]))[-2]