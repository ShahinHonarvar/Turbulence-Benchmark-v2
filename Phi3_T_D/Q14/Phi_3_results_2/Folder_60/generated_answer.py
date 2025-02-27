def find_second_smallest_num(nums):
    sorted_slice = sorted(nums[56:99])
    return sorted_slice[1] if len(sorted_slice) > 1 else None