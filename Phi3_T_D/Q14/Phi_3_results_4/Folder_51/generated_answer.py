def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    sorted_slice = sorted(nums[1:9])
    return sorted_slice[1] if len(set(sorted_slice)) > 1 else None