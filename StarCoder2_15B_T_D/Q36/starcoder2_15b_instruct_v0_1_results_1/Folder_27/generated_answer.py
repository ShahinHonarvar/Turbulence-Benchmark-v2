def filter_chars(input_string):
    result = ''
    for i, c in enumerate(input_string):
        if i < 48 or i >= 75 or (c <= '6' or c >= '_'):
            result += c
    return result