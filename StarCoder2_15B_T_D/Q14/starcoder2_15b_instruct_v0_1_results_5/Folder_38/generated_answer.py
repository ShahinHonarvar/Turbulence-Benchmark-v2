def find_second_smallest_num(nums):
    nums_slice = sorted(nums[37:52])
    if len(nums_slice) >= 2:
        return nums_slice[1]
    else:
        return None