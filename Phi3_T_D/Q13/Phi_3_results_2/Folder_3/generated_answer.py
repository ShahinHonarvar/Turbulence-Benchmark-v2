def find_second_largest_num(nums):
    start, end = (62, 92)
    if start > end or end >= len(nums):
        return None
    nums_slice = sorted(set(nums[start:end + 1]), reverse=True)
    return nums_slice[1] if len(nums_slice) > 1 else None