def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 7:
        return nums[6]
    else:
        return None