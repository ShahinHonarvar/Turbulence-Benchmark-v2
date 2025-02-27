def find_second_largest_num(nums):
    if len(nums) <= 7:
        return None
    nums = sorted(nums[0:8], reverse=True)
    return nums[1] if nums[1] != nums[0] else None