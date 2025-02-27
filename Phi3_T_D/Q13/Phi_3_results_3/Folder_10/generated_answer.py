def find_second_largest_num(nums):
    if len(nums) < 35:
        return None
    sub_nums = nums[25:60]
    sub_nums.sort(reverse=True)
    return sub_nums[1] if len(sub_nums) >= 2 else None