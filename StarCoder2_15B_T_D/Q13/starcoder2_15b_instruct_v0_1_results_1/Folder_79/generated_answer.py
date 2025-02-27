def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) >= 4:
        return nums[3]
    else:
        return None