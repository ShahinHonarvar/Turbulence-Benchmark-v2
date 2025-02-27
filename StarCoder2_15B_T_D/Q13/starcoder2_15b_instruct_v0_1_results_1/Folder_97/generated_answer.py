def find_second_largest_num(nums):
    sorted_sublist = sorted(nums[40:81], reverse=True)
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    else:
        return None