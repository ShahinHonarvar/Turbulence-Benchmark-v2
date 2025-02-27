def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 41:
        return None
    else:
        return sorted_nums[40]