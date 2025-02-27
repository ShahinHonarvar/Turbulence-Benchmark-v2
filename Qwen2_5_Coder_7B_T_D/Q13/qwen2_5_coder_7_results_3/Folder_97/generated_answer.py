def find_second_largest_num(nums):
    slice_nums = nums[40:81]
    if len(slice_nums) < 2:
        return None
    sorted_nums = sorted(slice_nums, reverse=True)
    return sorted_nums[1]