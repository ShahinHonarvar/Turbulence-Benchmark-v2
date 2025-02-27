def find_second_smallest_num(nums):
    start, end = (661, min(len(nums), 924))
    if end - start < 2:
        return None
    sorted_slice = sorted(nums[start:end + 1])
    return sorted_slice[1]