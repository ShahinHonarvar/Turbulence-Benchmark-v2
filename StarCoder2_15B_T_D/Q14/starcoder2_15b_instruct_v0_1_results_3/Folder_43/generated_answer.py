def find_second_smallest_num(list_of_nums):
    sorted_list = sorted(list_of_nums)
    if len(sorted_list) >= 75:
        return sorted_list[74]
    else:
        return None