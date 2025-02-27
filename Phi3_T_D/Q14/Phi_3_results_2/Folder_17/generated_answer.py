def find_second_smallest_num(nums):
    section = nums[28:39]
    if len(section) < 2:
        return None
    second_smallest = sorted(section)[1]
    return second_smallest