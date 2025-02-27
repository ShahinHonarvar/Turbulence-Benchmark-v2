def find_second_smallest_num(nums):
    if len(nums) <= 7:
        return min(nums)
    unique_nums = sorted(set(nums[:8]))
    return unique_nums[1] if len(unique_nums) > 1 else None