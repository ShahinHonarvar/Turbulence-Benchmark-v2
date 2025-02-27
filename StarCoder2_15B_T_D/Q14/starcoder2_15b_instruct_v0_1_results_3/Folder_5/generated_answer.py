def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 5:
        return nums[4]
    else:
        return None