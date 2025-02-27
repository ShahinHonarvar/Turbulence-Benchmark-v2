def find_second_smallest_num(nums):
    selected = nums[26:53]
    if len(selected) < 2:
        return None
    return sorted(selected)[1]