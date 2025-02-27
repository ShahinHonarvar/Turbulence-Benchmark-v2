def find_second_largest_num(nums):
    if len(nums) < 6 or len(set(nums[:6])) < 2:
        return None
    return sorted(set(nums[:6]))[-2]