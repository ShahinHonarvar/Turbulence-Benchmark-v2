def find_second_largest_num(nums):
    if 28 <= len(nums) <= 32:
        return sorted(nums[28:33], reverse=True)[1] if len(nums[28:33]) > 1 else None
    return None