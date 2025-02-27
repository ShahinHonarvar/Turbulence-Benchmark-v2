def find_largest_num(nums):
    if len(nums) > 7 and 5 <= len(nums) - 7:
        return max(nums[5:8])
    else:
        return None