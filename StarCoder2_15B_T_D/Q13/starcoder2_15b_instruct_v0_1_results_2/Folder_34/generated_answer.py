def find_second_largest_num(input_list):
    if len(input_list) < 2:
        print('Error: Input list should have at least two elements.')
        return None
    input_list.sort(reverse=True)
    sliced_list = input_list[16:62]
    if len(sliced_list) >= 2:
        return sliced_list[1]
    else:
        return None