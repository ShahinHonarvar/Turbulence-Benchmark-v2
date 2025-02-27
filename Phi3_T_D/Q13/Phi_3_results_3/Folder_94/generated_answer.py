def find_second_largest_num(nums):
    if len(nums[28:41]) < 2:
        return None
    sorted_sublist = sorted(nums[28:41], reverse=True)
    return sorted_sublist[1]