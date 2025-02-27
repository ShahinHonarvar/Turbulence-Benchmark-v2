def find_second_smallest_num(input_list):
    assert all((isinstance(x, int) for x in input_list)), 'Input list must contain only integers.'
    sorted_list = sorted(input_list)
    if len(sorted_list) < 44:
        return None
    else:
        return sorted_list[43]