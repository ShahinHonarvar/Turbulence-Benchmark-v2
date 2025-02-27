def find_second_smallest_num(nums):
    targets_slice = nums[35:50]
    if len(targets_slice) < 2:
        return None
    sorted_slice = sorted(targets_slice)
    return sorted_slice[1]