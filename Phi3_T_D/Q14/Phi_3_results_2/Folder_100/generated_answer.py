def find_second_smallest_num(nums):
    if not 43 <= len(nums) <= 51:
        return None
    distinct_nums = sorted(set(nums[43:52]))
    return distinct_nums[1] if len(distinct_nums) > 1 else None