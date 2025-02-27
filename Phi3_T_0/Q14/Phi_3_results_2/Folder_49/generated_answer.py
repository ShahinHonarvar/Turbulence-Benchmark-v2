def find_second_smallest_num(nums):
    if len(nums) < 121:
        return None
    sorted_slice = sorted(nums[80:201])
    return sorted_slice[1] if len(sorted_slice) > 1 else None