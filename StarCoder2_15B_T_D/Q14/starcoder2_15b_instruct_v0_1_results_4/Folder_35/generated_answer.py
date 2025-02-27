def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 25:
        return nums[19]
    else:
        return None