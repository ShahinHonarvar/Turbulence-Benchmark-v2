def find_second_smallest_num(nums):
    try:
        start_index = 33
        end_index = 36
        limited_nums = nums[start_index:end_index + 1]
        limited_nums.sort()
        return limited_nums[1] if len(limited_nums) >= 2 else None
    except (IndexError, ValueError):
        return None