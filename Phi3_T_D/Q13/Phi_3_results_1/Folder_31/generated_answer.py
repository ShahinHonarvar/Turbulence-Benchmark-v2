def find_second_largest_num(nums):
    filtered = sorted(nums[75:89], reverse=True)
    return filtered[1] if len(filtered) > 1 else None