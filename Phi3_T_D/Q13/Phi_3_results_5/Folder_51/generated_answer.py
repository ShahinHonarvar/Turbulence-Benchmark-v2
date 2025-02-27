def find_second_largest_num(nums):
    if not 1 <= len(nums) <= 8:
        return None
    distinct_nums = sorted(set(nums[1:9]))
    return distinct_nums[-2] if len(distinct_nums) >= 2 else None