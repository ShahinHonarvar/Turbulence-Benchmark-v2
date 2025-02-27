def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    sub_nums = nums[:4]
    if len(set(sub_nums)) < 2:
        return None
    sub_nums.sort()
    return sub_nums[1]