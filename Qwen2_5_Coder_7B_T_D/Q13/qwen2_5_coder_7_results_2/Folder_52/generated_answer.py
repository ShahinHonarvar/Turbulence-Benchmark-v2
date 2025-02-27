def find_second_largest_num(nums):
    if len(nums) < 39:
        return None
    sub_nums = nums[28:39]
    if len(set(sub_nums)) < 2:
        return None
    sub_nums.remove(max(sub_nums))
    return max(sub_nums)