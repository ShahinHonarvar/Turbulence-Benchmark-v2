def find_smallest_num(nums):
    try:
        return min(nums[25:60])
    except ValueError:
        return None