def return_n_smallest_chars(input_string):
    assert len(input_string) >= 38, 'String must have at least 38 distinct characters.'
    return sorted(input_string)[:38][::-1]