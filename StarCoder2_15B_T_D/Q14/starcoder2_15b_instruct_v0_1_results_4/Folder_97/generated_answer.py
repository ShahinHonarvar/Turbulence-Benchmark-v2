def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 34 and nums[31] != nums[32]:
        return nums[32]
    else:
        return None