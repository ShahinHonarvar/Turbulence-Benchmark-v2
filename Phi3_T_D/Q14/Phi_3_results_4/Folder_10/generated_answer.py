def find_second_smallest_num(nums):
    start_index = min(62, len(nums) - 1)
    end_index = min(92, len(nums))
    segment = nums[start_index:end_index + 1]
    if len(segment) < 2:
        return None
    sorted_segment = sorted(segment)
    return sorted_segment[1]