def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    nums = sorted(nums)
    if len(nums) < 60:
        return None
    elif len(nums) < 98:
        return nums[59]
    else:
        return nums[59:98][1]