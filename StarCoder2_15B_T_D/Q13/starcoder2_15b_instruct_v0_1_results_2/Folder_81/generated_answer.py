def find_second_largest_num(nums):
    nums = nums[10:101]
    nums.sort(reverse=True)
    if len(nums) >= 2:
        return nums[1]
    else:
        return None