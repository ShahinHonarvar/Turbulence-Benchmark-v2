def find_second_smallest_num(nums):
    sorted_part = sorted(nums[62:93])
    return sorted_part[1] if len(sorted_part) > 1 else None