def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    if len(sorted_nums) >= 93:
        return sorted_nums[12:93][1]
    else:
        return None