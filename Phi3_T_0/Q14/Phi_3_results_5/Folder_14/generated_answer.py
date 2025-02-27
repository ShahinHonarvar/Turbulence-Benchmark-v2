def find_second_smallest_num(nums):
    if len(nums) < 10:
        return None
    sorted_slice = sorted(nums[8:10])
    return sorted_slice[1] if len(sorted_slice) > 1 else None