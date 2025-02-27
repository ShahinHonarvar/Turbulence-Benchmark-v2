def find_second_largest_num(list_of_nums):
    sublist = list_of_nums[5:8]
    sorted_sublist = sorted(sublist, reverse=True)
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    else:
        return None