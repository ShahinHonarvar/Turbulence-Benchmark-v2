def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    nums.sort()
    if len(nums) >= 12:
        return nums[12]
    else:
        return None