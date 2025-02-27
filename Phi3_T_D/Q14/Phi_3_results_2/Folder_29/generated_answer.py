def find_second_smallest_num(nums):
    start, end = (55, min(len(nums), 98))
    if end - start < 2 or len(nums) < end:
        return None
    distinct_nums = sorted(set(nums[start:end + 1]))
    return distinct_nums[1] if len(distinct_nums) > 1 else None