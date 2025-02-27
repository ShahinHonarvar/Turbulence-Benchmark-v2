def find_second_smallest_num(nums):
    nums = sorted(nums[56:67])
    if len(nums) >= 2:
        return nums[1]
    else:
        return None