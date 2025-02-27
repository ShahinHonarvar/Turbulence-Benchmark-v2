def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    sublist = sorted_nums[15:40]
    if len(sublist) < 2:
        return None
    return sublist[1]