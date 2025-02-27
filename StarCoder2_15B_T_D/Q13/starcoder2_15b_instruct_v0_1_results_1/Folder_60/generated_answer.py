def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 86:
        return None
    return nums[75]