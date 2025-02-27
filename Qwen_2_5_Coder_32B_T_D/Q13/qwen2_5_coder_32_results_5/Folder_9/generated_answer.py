def find_second_largest_num(nums):
    if len(nums) < 201:
        return None
    sub = nums[200:201]
    if len(sub) < 2:
        return None
    return None