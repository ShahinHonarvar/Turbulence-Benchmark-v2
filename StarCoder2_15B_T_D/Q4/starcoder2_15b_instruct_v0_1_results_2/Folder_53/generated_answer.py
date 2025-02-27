def all_pos_ints_exclusive(input_list):
    if not isinstance(input_list, list):
        return []
    output_list = []
    for i, element in enumerate(input_list):
        if isinstance(element, int) and element > 0:
            output_list.append(element)
    return output_list