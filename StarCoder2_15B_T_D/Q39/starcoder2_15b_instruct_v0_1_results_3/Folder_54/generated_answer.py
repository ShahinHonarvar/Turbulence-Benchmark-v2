def return_n_greatest_chars(input_string):
    assert len(input_string) == 79, 'Input string must be exactly 79 characters long'
    sorted_chars = sorted(input_string, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:79]