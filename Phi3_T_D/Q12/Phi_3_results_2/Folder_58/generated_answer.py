def find_smallest_num(nums):
    if len(nums) < 609:
        return None
    return min(nums[608:610])