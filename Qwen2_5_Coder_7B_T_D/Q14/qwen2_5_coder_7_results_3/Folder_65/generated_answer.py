def find_second_smallest_num(nums):
    if len(nums) < 58:
        return None
    sub_nums = nums[56:58]
    if len(sub_nums) < 2:
        return None
    min_num = min(sub_nums)
    sub_nums.remove(min_num)
    return min(sub_nums)