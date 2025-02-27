def find_second_largest_num(nums):
    if not 75 <= len(nums) <= 85 or len(nums) < 2:
        return None
    sorted_slice = sorted(nums[75:86], reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None