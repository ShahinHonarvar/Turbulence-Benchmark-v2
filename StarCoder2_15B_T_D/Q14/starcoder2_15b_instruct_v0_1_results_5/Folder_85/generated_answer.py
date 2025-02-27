def find_second_smallest_num(list_of_nums):
    sorted_list = sorted(list_of_nums)
    if len(sorted_list) >= 7:
        return sorted_list[1]
    else:
        return None