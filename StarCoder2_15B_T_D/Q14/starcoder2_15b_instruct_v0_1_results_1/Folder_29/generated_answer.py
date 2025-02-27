def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 99:
        return nums[55:99][1]
    else:
        return None