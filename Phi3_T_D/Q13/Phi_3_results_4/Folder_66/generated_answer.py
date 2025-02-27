def find_second_largest_num(nums):
    if not 50 <= len(nums) <= 54:
        return None
    segment = nums[50:55]
    sorted_segment = sorted(segment, reverse=True)
    return sorted_segment[1] if len(sorted_segment) > 1 else None