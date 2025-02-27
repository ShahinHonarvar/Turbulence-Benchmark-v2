def find_second_smallest_num(input_list):
    assert len(input_list) >= 10, 'The input list must have at least 10 elements.'
    assert all((isinstance(x, int) for x in input_list)), 'The input list must contain only integers.'
    assert len(set(input_list)) == len(input_list), 'The input list must contain distinct elements.'
    sorted_list = sorted(input_list)
    second_smallest = sorted_list[82:87][1]
    return second_smallest