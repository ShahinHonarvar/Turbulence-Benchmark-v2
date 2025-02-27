def find_second_largest_num(input_list):
    sorted_list = sorted(input_list, reverse=True)
    if len(sorted_list) >= 2 and 66 < len(sorted_list):
        return sorted_list[10:67][1]
    else:
        return None