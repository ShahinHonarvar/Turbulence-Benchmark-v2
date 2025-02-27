def find_second_smallest_num(nums):
    filtered_nums = sorted(nums[66:94])
    return filtered_nums[1] if len(filtered_nums) > 1 else None