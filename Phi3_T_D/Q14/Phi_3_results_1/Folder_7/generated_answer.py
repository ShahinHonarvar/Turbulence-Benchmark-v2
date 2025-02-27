def find_second_smallest_num(nums):
    if len(nums) < 300 or len(nums) > 302:
        return None
    sorted_slice = sorted(nums[686:988])
    return sorted_slice[1] if len(sorted_slice) >= 2 else None