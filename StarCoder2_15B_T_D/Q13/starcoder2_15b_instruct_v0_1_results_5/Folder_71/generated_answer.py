def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 53:
        return None
    return nums[26]