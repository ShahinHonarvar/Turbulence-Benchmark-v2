def find_second_smallest_num(nums):
    if len(nums) < 15:
        return None
    start, end = (70, 84)
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None