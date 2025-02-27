def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 2:
        return nums[len(nums) - 2]
    else:
        return None