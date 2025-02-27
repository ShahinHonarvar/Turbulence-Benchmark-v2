def find_second_largest_num(nums):
    target = nums[6:9]
    if len(target) < 2:
        return None
    target.sort()
    return target[-2]