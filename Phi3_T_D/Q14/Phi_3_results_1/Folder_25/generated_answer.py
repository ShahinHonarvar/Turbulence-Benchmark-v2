def find_second_smallest_num(nums):
    if 37 <= len(nums) <= 76:
        sub_nums = nums[37 - 1:77]
        return sorted(set(sub_nums))[1] if len(set(sub_nums)) > 1 else None
    return None