def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[22:51][1] if len(sorted_nums[22:51]) >= 2 else None