def find_second_largest_num(nums):
    if len(nums) < 57:
        return None
    start, end = (10, 66)
    nums = sorted(nums[start:end + 1], reverse=True)
    return nums[1] if len(nums) > 1 else None