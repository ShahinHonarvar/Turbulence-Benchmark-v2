def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 27:
        return None
    return nums[26]