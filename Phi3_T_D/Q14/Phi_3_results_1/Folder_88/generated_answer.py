def find_second_smallest_num(nums):
    start, end = (6, 8)
    if len(nums[start:end + 1]) < 2:
        return None
    sorted_subset = sorted(nums[start:end + 1])
    return sorted_subset[1] if sorted_subset[1] != sorted_subset[0] else None