def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    sorted_nums = sorted(nums[:4])
    return sorted_nums[1] if len(sorted_nums) > 1 else None