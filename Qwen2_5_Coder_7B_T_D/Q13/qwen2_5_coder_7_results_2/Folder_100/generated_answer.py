def find_second_largest_num(nums):
    if len(nums) < 69:
        return None
    sub_nums = nums[42:69]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort()
    return sub_nums[-2]