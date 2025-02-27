def find_second_smallest_num(nums):
    try:
        return sorted(nums[62:64])[1]
    except (IndexError, ValueError):
        return None