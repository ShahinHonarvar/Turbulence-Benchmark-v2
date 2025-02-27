def find_second_smallest_num(nums):
    start, end = (31, min(len(nums), 73))
    if end - start < 2:
        return None
    sorted_slice = sorted(nums[start:end])
    return sorted_slice[1]