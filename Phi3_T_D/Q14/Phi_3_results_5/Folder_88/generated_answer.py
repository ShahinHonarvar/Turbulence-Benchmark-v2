def find_second_smallest_num(nums):
    target_slice = nums[6:9]
    if len(target_slice) < 2:
        return None
    sorted_slice = sorted(target_slice)
    return sorted_slice[1]