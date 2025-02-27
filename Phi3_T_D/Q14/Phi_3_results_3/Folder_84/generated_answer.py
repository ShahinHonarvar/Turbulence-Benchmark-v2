def find_second_smallest_num(nums):
    if len(nums) < 41:
        return None
    segment = nums[40:81]
    unique_segment = sorted(set(segment))
    return unique_segment[1] if len(unique_segment) > 1 else None