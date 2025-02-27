def find_second_largest_num(nums):
    if len(nums) <= 90:
        return None
    target_slice = nums[90:91]
    if len(target_slice) < 2:
        return None
    target_slice.sort()
    return target_slice[-2]