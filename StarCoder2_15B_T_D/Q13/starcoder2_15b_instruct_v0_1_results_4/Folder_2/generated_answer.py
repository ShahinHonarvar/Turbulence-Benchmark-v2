def find_second_largest_num(input_list):
    input_list.sort(reverse=True)
    if len(input_list) >= 20:
        return input_list[19]
    else:
        return None