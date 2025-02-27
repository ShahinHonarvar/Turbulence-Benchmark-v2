def find_second_largest_num(nums):
    start_index = 6
    end_index = 8
    if end_index >= len(nums):
        return None
    sub_nums = nums[start_index:end_index + 1]
    if len(set(sub_nums)) < 2:
        return None
    return sorted(set(sub_nums), reverse=True)[1]