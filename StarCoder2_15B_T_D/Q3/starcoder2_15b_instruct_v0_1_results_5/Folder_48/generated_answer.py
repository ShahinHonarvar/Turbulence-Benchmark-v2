def all_pos_ints_inclusive(input_list):
    output_list = []
    for element in input_list:
        if element > 0:
            output_list.append(element)
    return output_list