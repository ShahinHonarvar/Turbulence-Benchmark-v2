def find_second_largest_num(nums):
    if len(nums[22:89]) < 2:
        return None
    sorted_slice = sorted(nums[22:89])
    return sorted_slice[-2]