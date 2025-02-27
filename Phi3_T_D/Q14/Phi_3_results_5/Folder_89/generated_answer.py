def find_second_smallest_num(nums):
    start, end = (62, 63)
    slice_of_nums = nums[start:end + 1]
    sorted_slice = sorted(slice_of_nums)
    return min(sorted_slice[1], (None, None)[len(sorted_slice) < 2])