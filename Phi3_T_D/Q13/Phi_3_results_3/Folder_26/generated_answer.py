def find_second_largest_num(nums):
    target_slice = nums[62:100]
    if len(target_slice) < 2:
        return None
    target_slice.sort()
    return target_slice[-2]