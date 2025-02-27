def find_second_smallest_num(nums):
    if len(nums) > 4:
        nums = nums[:4]
    nums = sorted(set(nums))
    return nums[1] if len(nums) > 1 else None