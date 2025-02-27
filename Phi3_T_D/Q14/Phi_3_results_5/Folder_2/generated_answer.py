def find_second_smallest_num(nums):
    if len(nums[43:87]) < 2:
        return None
    sorted_slice = sorted(nums[43:86])
    return sorted_slice[1]