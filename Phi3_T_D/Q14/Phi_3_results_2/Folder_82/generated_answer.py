def find_second_smallest_num(nums):
    valid_part = nums[20:201]
    if len(valid_part) >= 2:
        valid_part.sort()
        return valid_part[1]
    return None