def find_second_smallest_num(nums):
    if len(nums) <= 2 or len(nums) > 8:
        return None
    sorted_nums = sorted(nums[:8])
    return sorted_nums[1] if len(sorted_nums) > 1 else None