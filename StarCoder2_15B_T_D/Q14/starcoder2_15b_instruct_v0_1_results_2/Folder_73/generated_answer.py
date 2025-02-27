def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 98:
        return nums[59]
    else:
        return None