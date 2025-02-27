def find_second_largest_num(nums):
    nums = sorted(nums)[::-1]
    if len(nums) >= 40:
        return nums[40]
    else:
        return None