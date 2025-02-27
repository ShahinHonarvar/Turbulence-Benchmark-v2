def find_second_smallest_num(list_of_nums):
    sorted_list = sorted(list_of_nums)
    if len(sorted_list) >= 88:
        return sorted_list[87]
    else:
        return None