def find_second_largest_num(nums):
    sorted_slice = sorted(nums[25:60], reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None