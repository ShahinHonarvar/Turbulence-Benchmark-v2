def find_second_smallest_num(nums):
    if len(nums) > 57:
        slice_nums = sorted(nums[56:57 + 1])
        if len(slice_nums) > 1:
            return slice_nums[1]
        return None
    return None