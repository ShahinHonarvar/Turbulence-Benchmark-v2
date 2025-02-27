def find_second_smallest_num(nums):
    valid_range = nums[37:77]
    if len(valid_range) < 2:
        return None
    second_smallest = sorted(valid_range)[1]
    return second_smallest