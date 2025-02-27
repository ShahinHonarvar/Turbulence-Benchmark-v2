def find_second_smallest_num(nums):
    sub_nums = nums[66:94]
    if len(sub_nums) < 2:
        return None
    sorted_nums = sorted(set(sub_nums))
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]