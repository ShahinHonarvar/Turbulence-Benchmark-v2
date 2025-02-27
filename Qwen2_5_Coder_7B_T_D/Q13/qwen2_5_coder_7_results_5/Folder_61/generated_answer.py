def find_second_largest_num(nums):
    return sorted(nums[:8], reverse=True)[1] if len(nums[:8]) > 1 else None