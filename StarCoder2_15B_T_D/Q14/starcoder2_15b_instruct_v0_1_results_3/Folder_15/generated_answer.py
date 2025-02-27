def find_second_smallest_num(nums):
    nums[:4].sort()
    return nums[1] if len(nums) >= 4 else None