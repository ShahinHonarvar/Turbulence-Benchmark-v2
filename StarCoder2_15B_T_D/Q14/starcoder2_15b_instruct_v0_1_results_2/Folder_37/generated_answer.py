def find_second_smallest_num(list_of_nums):
    sorted_sublist = sorted(list_of_nums[5:8])
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]