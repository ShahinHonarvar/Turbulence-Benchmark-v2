def find_second_largest_num(input_list):
    input_list.sort(reverse=True)
    if len(input_list) < 67:
        return None
    else:
        return input_list[66]