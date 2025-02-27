def find_second_largest_num(nums):
    sub_nums = nums[10:67]
    if len(sub_nums) < 2:
        return None
    sub_nums.remove(max(sub_nums))
    return max(sub_nums)