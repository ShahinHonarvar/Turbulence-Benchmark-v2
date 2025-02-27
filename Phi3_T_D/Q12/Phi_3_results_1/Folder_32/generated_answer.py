def find_smallest_num(nums):
    if len(nums) < 63:
        return None
    return min(nums[25:88])