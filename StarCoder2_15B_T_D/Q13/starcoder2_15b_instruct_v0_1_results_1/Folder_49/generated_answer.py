def find_second_largest_num(input_list):
    input_list.sort(reverse=True)
    if len(input_list) >= 201 - 80 + 1:
        return input_list[80 + 1]
    else:
        return None