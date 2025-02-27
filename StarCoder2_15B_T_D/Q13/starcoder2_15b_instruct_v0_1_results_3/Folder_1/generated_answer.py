def find_second_largest_num(nums):
    nums = sorted(nums)[::-1]
    if len(nums) >= 2:
        return nums[1]
    return None