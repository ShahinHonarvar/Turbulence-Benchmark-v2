def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) >= 58:
        return nums[57]
    else:
        return None