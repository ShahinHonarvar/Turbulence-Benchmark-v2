def find_second_smallest_num(nums):
    if len(nums) < 13:
        return None
    start, end = (28, min(40, len(nums)))
    sorted_slice = sorted(nums[start:end + 1])
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]