def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    sorted_nums = sorted(nums[4:6], reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None