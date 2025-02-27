def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 36:
        return nums[34]
    else:
        return None