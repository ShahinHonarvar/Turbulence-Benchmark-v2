def find_second_largest_num(nums):
    principal_slice = nums[22:51]
    if len(principal_slice) < 2:
        return None
    principal_slice.sort()
    return principal_slice[-2] if principal_slice[-1] != principal_slice[-2] else principal_slice[-3]