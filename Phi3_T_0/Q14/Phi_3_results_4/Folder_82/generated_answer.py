def find_second_smallest_num(nums):
    if len(nums) < 202:
        return None
    sorted_nums = sorted(nums[20:201])
    return sorted_nums[1] if len(sorted_nums) > 1 else None