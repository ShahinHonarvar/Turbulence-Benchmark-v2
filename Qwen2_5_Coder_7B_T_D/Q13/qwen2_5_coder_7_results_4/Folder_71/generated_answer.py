def find_second_largest_num(nums):
    if len(nums) < 27 or len(nums) > 53:
        return None
    sub_nums = nums[26:53]
    sorted_nums = sorted(set(sub_nums), reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]