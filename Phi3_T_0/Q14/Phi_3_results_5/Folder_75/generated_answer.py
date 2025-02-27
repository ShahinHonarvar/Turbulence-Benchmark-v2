def find_second_smallest_num(nums):
    if len(nums) < 12 or len(nums) > 92:
        return None
    sorted_nums = sorted(nums[11:93])
    return sorted_nums[1] if len(sorted_nums) > 1 else None