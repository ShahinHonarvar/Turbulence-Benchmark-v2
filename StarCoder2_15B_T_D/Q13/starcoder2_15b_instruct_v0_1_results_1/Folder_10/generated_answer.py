def find_second_largest_num(list_of_nums):
    sorted_list = sorted(list_of_nums, reverse=True)
    if len(sorted_list) < 59:
        return None
    return sorted_list[1]