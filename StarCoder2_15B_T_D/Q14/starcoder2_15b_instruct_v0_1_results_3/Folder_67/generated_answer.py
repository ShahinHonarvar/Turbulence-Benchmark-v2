def find_second_smallest_num(list_of_nums):
    sublist = sorted(list_of_nums[50:55])
    return sublist[1] if len(sublist) == 5 else None