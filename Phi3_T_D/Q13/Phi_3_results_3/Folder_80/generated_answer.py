def find_second_largest_num(nums):
    start_index, end_index = (64, 66)
    if start_index < len(nums) and end_index < len(nums):
        sub_nums = sorted(nums[start_index:end_index + 1], reverse=True)
        return sub_nums[1] if len(sub_nums) > 1 else None
    return None