def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sorted_slice = sorted(nums[8:10], reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None