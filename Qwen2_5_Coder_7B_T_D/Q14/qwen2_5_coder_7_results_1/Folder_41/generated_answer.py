def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    sub_nums = sorted(nums[4:5])
    if len(sub_nums) < 2:
        return None
    return sub_nums[1]