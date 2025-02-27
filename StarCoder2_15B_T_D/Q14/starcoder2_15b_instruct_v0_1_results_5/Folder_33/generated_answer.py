def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) < 263:
        return None
    return nums[262]