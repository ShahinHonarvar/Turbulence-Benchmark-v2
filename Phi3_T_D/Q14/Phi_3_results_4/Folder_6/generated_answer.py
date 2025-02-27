def find_second_smallest_num(nums):
    start, end = (29, min(len(nums), 79))
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1] if len(sorted_slice) > 1 else None