def find_second_smallest_num(nums):
    sub_nums = nums[12:93]
    if len(sub_nums) < 2:
        return None
    sub_nums.remove(min(sub_nums))
    return min(sub_nums)