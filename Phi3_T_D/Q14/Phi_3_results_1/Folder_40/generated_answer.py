def find_second_smallest_num(nums):
    unique_nums = sorted(set(nums[:3]))
    return unique_nums[1] if len(unique_nums) > 1 else None