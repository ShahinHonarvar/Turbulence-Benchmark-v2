def find_second_largest_num(nums):
    slice_of_nums = nums[52:72]
    if len(slice_of_nums) < 2:
        return None
    slice_of_nums.sort()
    return slice_of_nums[-2]