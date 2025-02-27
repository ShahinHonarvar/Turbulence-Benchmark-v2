def find_second_largest_num(nums):
    start, end = (30, 200)
    if end >= len(nums) or start >= len(nums):
        return None
    sorted_slice = sorted(nums[start:end + 1], reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None