def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) > 97:
        return nums[1]
    return None