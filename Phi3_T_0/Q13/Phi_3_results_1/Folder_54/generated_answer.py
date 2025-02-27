def find_second_largest_num(nums):
    if len(nums) < 22:
        return None
    sorted_slice = sorted(nums[34:55], reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None