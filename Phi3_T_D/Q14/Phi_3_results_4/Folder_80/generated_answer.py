def find_second_smallest_num(nums):
    start, end = (30, 87)
    if start >= len(nums) or end < start or end >= len(nums):
        return None
    distinct_nums = sorted(set(nums[start:end + 1]))
    return distinct_nums[1] if len(distinct_nums) > 1 else None