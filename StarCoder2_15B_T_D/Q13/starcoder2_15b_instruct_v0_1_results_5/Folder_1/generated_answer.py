def find_second_largest_num(nums):
    nums = sorted(nums, reverse=True)
    if len(nums) < 32:
        return None
    return nums[31]