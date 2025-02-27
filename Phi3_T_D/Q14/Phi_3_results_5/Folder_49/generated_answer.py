def find_second_smallest_num(nums):
    valid_slice = nums[80:201]
    if len(valid_slice) < 2:
        return None
    valid_slice.sort()
    return valid_slice[1]