def find_second_smallest_num(list_of_nums):
    sublist = list_of_nums[262:747]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]