def find_second_smallest_num(nums):
    if len(nums[33:37]) < 2:
        return None
    second_smallest = sorted(nums[33:37])[1]
    return second_smallest