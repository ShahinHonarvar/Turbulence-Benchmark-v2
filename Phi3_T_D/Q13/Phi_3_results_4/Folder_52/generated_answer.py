def find_second_largest_num(nums):
    start, end = (28, 38)
    valid_range_nums = nums[start:end + 1]
    if not valid_range_nums or len(set(valid_range_nums)) < 2:
        return None
    return sorted(set(valid_range_nums))[-2]