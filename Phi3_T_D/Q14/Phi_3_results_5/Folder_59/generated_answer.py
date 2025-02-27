def find_second_smallest_num(nums):
    if not isinstance(nums, list) or len(nums) < 10:
        return None
    sorted_nums = sorted(nums[:10])
    if len(sorted_nums) > 1:
        return sorted_nums[1]
    return None