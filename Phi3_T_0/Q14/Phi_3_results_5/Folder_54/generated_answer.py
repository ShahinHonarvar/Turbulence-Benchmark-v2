def find_second_smallest_num(nums):
    start, end = (68, min(len(nums), 86))
    if end - start < 2:
        return None
    sorted_slice = sorted(nums[start:end])
    return sorted_slice[1]