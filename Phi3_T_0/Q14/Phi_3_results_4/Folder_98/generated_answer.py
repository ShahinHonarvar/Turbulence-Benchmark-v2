def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    sorted_slice = sorted(nums[6:7])
    return sorted_slice[0] if len(sorted_slice) > 1 else None