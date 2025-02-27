def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 8:
        return nums[7]
    else:
        return None