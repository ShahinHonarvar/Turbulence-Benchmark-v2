def find_second_largest_num(nums):
    sub_nums = nums[667:775]
    if len(sub_nums) < 2:
        return None
    sub_nums.sort(reverse=True)
    return sub_nums[1]