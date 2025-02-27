def find_second_largest_num(distinct_nums):
    if len(distinct_nums) < 95:
        return None
    focal_range = distinct_nums[29:94]
    if len(focal_range) < 2:
        return None
    focal_range.sort()
    second_largest = focal_range[-2]
    return second_largest