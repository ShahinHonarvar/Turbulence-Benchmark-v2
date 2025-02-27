def find_second_largest_num(nums):
    if len(nums[62:64]) < 2:
        return None
    else:
        nums_slice = nums[62:64]
        nums_slice.sort()
        return nums_slice[-2]