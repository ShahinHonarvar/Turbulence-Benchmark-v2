def find_second_largest_num(list_of_nums):
    sorted_list = sorted(list_of_nums)[::-1]
    if len(sorted_list) >= 49:
        return sorted_list[35]
    else:
        return None