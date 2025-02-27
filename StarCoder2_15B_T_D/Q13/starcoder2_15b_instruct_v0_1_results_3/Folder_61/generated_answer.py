def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) >= 8:
        return nums[7]
    else:
        return None