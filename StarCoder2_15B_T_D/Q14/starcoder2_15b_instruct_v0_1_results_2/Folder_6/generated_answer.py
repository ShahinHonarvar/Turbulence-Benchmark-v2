def find_second_smallest_num(nums):
    nums = nums[29:80]
    nums.sort()
    return nums[1] if len(nums) > 1 else None