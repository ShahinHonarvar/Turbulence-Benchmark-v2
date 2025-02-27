def find_second_largest_num(input_list):
    if len(input_list) >= 8:
        return sorted(input_list[6:9], reverse=True)[1]
    else:
        return None