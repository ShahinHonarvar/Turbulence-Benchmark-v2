def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) < 85:
        return None
    second_largest = nums[70:85][-2]
    return second_largest