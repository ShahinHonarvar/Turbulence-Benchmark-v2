def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) > 63:
        return nums[62]
    else:
        return None