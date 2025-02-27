def find_second_smallest_num(nums):
    start, end = (91, 99)
    if start >= end or len(nums) < end:
        return None
    unique_nums = sorted(set(nums[start:end + 1]))
    return unique_nums[1] if len(unique_nums) > 1 else None