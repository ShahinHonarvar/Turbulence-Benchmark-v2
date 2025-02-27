def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 22:
        return nums[22]
    else:
        return None