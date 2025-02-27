def find_second_smallest_num(nums):
    sorted_nums = sorted(nums)
    sublist = sorted_nums[19:93]
    if len(sublist) < 2:
        return None
    return sublist[1]