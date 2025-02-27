def find_second_smallest_num(nums):
    sorted_nums = sorted(nums[56:67])
    return sorted_nums[1] if len(sorted_nums) >= 2 else None