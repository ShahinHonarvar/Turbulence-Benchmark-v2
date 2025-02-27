def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 34:
        return nums[32]
    else:
        return None