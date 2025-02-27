def find_second_largest_num(input_list):
    sorted_list = sorted(input_list[70:85], reverse=True)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None