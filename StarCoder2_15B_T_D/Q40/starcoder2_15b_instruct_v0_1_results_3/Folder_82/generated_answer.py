def return_n_smallest_chars(input_string):
    assert len(input_string) >= 60, 'Input string must be at least 60 characters long'
    sorted_string = sorted(input_string)
    return sorted_string[:60]