def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) > 82:
        return nums[82]
    elif len(nums) > 56:
        return nums[56]
    else:
        return None