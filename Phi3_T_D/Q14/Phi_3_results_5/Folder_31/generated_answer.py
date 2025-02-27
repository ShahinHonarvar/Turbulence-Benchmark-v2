def find_second_smallest_num(nums):
    valid_nums = nums[29:94]
    if len(valid_nums) < 2:
        return None
    sorted_nums = sorted(valid_nums)
    return sorted_nums[1]