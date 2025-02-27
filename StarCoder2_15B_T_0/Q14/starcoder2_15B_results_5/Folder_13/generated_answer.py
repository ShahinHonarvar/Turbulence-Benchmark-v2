def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 33:
        return nums[28]
    else:
        return None