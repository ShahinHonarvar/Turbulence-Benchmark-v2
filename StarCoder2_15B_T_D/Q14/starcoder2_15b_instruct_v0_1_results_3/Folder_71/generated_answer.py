def find_second_smallest_num(nums):
    if len(nums) < 62:
        return None
    sorted_nums = sorted(nums[29:52])
    return sorted_nums[1]