def find_second_largest_num(nums):
    if len(nums) < 15 or len(nums) > 15:
        return None
    sub_nums = nums[34:50]
    max_num = max(sub_nums)
    sub_nums.remove(max_num)
    return max(sub_nums) if sub_nums else None