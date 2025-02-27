def find_second_smallest_num(nums):
    start, end = (22, min(88, len(nums)))
    if end - start < 2:
        return None
    sorted_slice = sorted(nums[start:end])
    return sorted_slice[1]