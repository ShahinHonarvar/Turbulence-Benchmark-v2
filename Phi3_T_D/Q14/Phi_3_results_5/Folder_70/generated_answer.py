def find_second_smallest_num(nums):
    target_slice = nums[35:50]
    if len(target_slice) < 2:
        return None
    second_smallest = sorted(target_slice)[1]
    return second_smallest