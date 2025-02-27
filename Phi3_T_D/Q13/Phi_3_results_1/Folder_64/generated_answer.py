def find_second_largest_num(nums):
    if len(nums) > 5:
        return max((n for n in nums[0:5] if n != max(nums[0:5])))
    return None