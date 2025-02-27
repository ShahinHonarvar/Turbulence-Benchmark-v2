def find_second_smallest_num(nums):
    distinct_nums = sorted(set(nums[:8]))
    return distinct_nums[1] if len(distinct_nums) > 1 else None