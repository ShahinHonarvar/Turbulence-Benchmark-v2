def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[62:93][1]