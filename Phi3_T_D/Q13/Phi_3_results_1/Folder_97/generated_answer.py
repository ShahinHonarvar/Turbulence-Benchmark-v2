def find_second_largest_num(nums):
    if len(nums) < 41:
        return None
    select_range = nums[40:81]
    distinct_sorted = sorted(set(select_range), reverse=True)
    return distinct_sorted[1] if len(distinct_sorted) > 1 else None