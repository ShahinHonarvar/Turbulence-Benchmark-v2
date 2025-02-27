def find_second_smallest_num(nums):
    if len(nums) < 26 or len(nums) > 98:
        return None
    sorted_nums = sorted(nums[20:26])
    return sorted_nums[1] if len(sorted_nums) > 1 else None