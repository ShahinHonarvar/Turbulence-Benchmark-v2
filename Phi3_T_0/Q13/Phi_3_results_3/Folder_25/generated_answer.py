def find_second_largest_num(nums):
    if len(nums) < 95 or len(nums) > 100:
        return None
    start, end = (29, 93)
    nums = nums[start:end + 1]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]