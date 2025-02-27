def find_second_smallest_num(nums):
    sorted_slice = sorted(nums[70:85])
    return sorted_slice[1] if len(sorted_slice) > 1 else None