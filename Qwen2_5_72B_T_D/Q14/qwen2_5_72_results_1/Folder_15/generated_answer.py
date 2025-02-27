def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    slice_nums = nums[:4]
    slice_nums.sort()
    return slice_nums[1] if len(slice_nums) > 1 else None