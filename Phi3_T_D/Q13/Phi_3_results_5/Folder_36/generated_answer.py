def find_second_largest_num(nums):
    start, end = (246, 750)
    if start >= end or len(nums[start:end + 1]) < 2:
        return None
    sorted_subset = sorted(nums[start:end + 1], reverse=True)
    return sorted_subset[1]