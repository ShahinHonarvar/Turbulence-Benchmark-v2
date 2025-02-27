def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) >= 10:
        return nums[8]
    else:
        return None