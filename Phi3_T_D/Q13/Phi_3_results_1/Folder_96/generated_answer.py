def find_second_largest_num(nums):
    if len(nums[15:52]) < 2:
        return None
    slice_nums = sorted(nums[15:52], reverse=True)
    return slice_nums[1]