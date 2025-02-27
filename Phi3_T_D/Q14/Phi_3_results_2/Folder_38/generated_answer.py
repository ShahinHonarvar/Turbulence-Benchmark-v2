def find_second_smallest_num(nums):
    slice_range = nums[37:52]
    if len(slice_range) < 2:
        return None
    sorted_slice = sorted(slice_range)
    second_smallest = sorted_slice[1]
    return second_smallest