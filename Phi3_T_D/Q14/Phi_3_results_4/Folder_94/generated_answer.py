def find_second_smallest_num(nums):
    if not 52 <= len(nums) <= 71:
        return None
    sorted_slice = sorted(nums[52:72])
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]