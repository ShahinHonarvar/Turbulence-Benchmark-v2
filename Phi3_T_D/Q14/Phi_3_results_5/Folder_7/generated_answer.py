def find_second_smallest_num(nums):
    start, end = (686, min(len(nums), 987))
    distinct_nums = sorted(set(nums[start:end + 1]))
    return distinct_nums[1] if len(distinct_nums) > 1 else None