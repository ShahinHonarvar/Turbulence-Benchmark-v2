def find_second_smallest_num(nums):
    if len(nums[50:201]) < 2:
        return None
    subset = sorted(nums[50:201])
    return subset[1]