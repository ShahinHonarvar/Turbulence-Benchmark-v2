def find_second_largest_num(nums):
    nums = nums[:9]
    nums.sort(reverse=True)
    if len(nums) > 1:
        return nums[1]
    else:
        return None