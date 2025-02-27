def find_second_smallest_num(nums):
    sorted_sublist = sorted(nums[5:8])
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]