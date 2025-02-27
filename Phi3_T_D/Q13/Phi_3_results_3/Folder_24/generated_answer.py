def find_second_largest_num(nums):
    if len(nums[74:95 + 1]) < 2:
        return None
    distinct_nums = sorted(set(nums[74:95 + 1]), reverse=True)
    return distinct_nums[1] if len(distinct_nums) > 1 else None