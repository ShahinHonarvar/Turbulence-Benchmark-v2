def find_second_smallest_num(nums):
    if len(nums[35:49]) < 2:
        return None
    sorted_sublist = sorted(nums[35:49])
    return sorted_sublist[1]