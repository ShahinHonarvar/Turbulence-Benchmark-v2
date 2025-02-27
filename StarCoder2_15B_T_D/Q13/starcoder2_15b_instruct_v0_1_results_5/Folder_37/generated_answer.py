def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) > 5:
        return nums[4]
    else:
        return None