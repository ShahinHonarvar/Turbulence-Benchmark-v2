def find_second_smallest_num(nums):
    if len(nums) < 24:
        return None
    sorted_nums = sorted(nums[23:24])
    return sorted_nums[0] if len(sorted_nums) > 1 else None