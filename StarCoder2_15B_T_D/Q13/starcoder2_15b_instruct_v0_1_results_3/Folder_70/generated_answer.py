def find_second_largest_num(nums):
    nums = sorted(nums, reverse=True)
    if len(nums) >= 3:
        return nums[2]
    else:
        return None