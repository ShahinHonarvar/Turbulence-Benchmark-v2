def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    target_slice = nums[64:67]
    if len(target_slice) < 2:
        return None
    target_slice.sort()
    return target_slice[-2]