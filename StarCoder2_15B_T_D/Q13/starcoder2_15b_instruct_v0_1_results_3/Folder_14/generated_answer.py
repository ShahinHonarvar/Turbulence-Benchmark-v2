def find_second_largest_num(nums):
    nums = sorted(nums, reverse=True)
    if len(nums) >= 8:
        return nums[5]
    else:
        return None