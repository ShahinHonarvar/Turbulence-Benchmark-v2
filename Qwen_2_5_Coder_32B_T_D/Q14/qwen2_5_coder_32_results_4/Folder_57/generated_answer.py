def find_second_smallest_num(nums):
    if len(nums) < 31:
        return None
    sub = nums[20:31]
    sub.sort()
    return sub[1] if len(sub) > 1 else None