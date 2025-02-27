def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sub_nums = nums[6:9]
    sub_nums.sort()
    return sub_nums[-2] if len(sub_nums) > 1 else None