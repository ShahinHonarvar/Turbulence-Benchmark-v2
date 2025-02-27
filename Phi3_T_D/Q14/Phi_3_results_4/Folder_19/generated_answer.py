def find_second_smallest_num(nums):
    if len(nums) < 9 or len(nums) > 9:
        return None
    c = nums[4:9]
    if len(c) < 2:
        return None
    c = sorted(c)
    return c[1]