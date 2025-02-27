def find_second_smallest_num(nums):
    start, end = (639, min(len(nums), 975))
    if end - start < 2:
        return None
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1]