def find_second_smallest_num(nums):
    if len(nums) < 61:
        return None
    sorted_slice = sorted(nums[309:371])
    return sorted_slice[1] if len(sorted_slice) > 1 else None