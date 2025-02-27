def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) < 2 or len(nums[1:6]) < 2:
        return None
    return nums[1:6][-2]