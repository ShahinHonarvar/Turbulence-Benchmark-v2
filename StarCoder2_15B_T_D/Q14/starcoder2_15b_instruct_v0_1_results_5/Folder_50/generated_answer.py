def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) >= 42:
        return nums[42]
    else:
        return None