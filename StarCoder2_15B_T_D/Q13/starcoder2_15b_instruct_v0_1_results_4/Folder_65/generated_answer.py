def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) > 98:
        return nums[97]
    else:
        return None