def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 58:
        return nums[57]
    else:
        return None