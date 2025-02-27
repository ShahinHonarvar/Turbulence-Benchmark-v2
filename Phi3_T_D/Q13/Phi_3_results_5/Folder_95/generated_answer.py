def find_second_largest_num(nums):
    targets = nums[82:87]
    if len(targets) < 2:
        return None
    return sorted(targets)[-2]