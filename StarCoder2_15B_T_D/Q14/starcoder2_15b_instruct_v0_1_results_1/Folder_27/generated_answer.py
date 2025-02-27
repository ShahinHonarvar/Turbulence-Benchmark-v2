def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 40:
        return nums[25 + 1]
    else:
        return None