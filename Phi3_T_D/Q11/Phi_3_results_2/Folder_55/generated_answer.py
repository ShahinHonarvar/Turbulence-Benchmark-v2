def find_largest_num(nums):
    if len(nums) > 11:
        return max(nums[:11])
    else:
        return max(nums)