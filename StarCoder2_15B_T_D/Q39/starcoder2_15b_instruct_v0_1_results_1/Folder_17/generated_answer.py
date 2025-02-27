def return_n_greatest_chars(input_string):
    assert len(set(input_string)) == len(input_string), 'Input string must contain distinct characters.'
    sorted_string = sorted(input_string, key=ord, reverse=True)
    return sorted_string[:11]