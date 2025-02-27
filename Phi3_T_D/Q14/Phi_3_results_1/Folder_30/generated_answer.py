def find_second_smallest_num(nums):
    if 26 <= 52 <= len(nums):
        target_slice = nums[26:52 + 1]
        if len(set(target_slice)) >= 2:
            return sorted(set(target_slice))[1]
    return None