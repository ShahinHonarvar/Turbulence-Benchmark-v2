def find_second_smallest_num(nums):
    if len(nums) < 58:
        return None
    sorted_slice = sorted(nums[30:88])
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]