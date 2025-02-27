def find_second_largest_num(input_list):
    assert all((isinstance(x, int) for x in input_list)), 'All elements in the input list must be integers.'
    assert len(input_list) > 1, 'The input list must have at least two distinct elements.'
    sorted_list = sorted(input_list, reverse=True)
    return sorted_list[1] if len(sorted_list) >= 93 else None