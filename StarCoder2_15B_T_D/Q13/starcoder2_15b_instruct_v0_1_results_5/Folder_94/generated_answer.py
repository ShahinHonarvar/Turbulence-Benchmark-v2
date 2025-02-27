def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 41:
        return nums[39]
    else:
        return None