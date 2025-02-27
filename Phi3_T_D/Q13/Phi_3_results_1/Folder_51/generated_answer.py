def find_second_largest_num(nums):
    valid_range_nums = nums[1:9]
    if len(valid_range_nums) < 2:
        return None
    return sorted(valid_range_nums)[-2]