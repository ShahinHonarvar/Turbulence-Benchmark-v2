def find_second_largest_num(nums):
    if len(nums[75:88]) < 2:
        return None
    truncated_nums = sorted(nums[75:88], reverse=True)
    return truncated_nums[1]