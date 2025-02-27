def find_second_largest_num(nums):
    nums.sort()
    if len(nums) > 8:
        return nums[7]
    return None