def find_second_largest_num(nums):
    valid_slice = nums[34:56]
    if len(valid_slice) < 2:
        return None
    valid_slice.sort()
    return valid_slice[-2]