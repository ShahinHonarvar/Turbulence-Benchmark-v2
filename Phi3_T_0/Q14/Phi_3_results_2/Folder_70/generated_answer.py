def find_second_smallest_num(nums):
    start, end = (35, 49)
    if end >= len(nums):
        end = len(nums) - 1
    if end - start < 1:
        return None
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None