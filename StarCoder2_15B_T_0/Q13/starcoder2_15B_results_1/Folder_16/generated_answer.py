def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 36:
        return nums[35]
    else:
        return None