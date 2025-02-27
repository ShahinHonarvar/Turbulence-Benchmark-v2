def find_second_largest_num(nums):
    nums = sorted(nums)[::-1]
    if len(nums) < 7:
        return None
    return nums[6]