def find_smallest_num(nums):
    try:
        return min(nums[62:99])
    except (ValueError, IndexError):
        return None