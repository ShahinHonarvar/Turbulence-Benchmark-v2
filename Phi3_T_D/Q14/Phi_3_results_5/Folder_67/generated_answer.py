def find_second_smallest_num(nums):
    return min(nums[50:55], default=None, key=lambda x: x) if len(nums[50:55]) > 1 else None