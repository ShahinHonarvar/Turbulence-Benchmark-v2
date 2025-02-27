def all_pos_ints_exclusive(nums):
    filtered_nums = list(filter(lambda x: x > 0, nums))
    if len(filtered_nums) > 0:
        return filtered_nums[2:8]
    else:
        return []