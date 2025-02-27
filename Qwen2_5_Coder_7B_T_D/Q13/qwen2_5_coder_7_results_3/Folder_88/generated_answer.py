def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sub_nums = nums[4:9]
    if len(sub_nums) < 2:
        return None
    sub_nums.remove(max(sub_nums))
    return max(sub_nums)