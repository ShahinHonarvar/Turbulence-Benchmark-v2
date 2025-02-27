def return_n_greatest_chars(input_string):
    assert len(set(input_string)) == len(input_string), 'Input string must contain distinct characters'
    assert len(input_string) >= 76, 'Input string must be at least 76 characters long'
    sorted_chars = sorted(input_string, key=ord, reverse=True)
    return sorted_chars[:76]