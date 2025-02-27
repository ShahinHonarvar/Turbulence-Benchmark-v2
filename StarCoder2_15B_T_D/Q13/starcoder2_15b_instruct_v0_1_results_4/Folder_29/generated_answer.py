def find_second_largest_num(input_list):
    input_list.sort(reverse=True)
    if len(input_list) >= 98:
        return input_list[97]
    else:
        return None