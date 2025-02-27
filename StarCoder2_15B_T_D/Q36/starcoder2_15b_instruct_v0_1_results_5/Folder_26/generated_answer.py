def filter_chars(input_string):
    filtered_chars = []
    for char in input_string:
        if char <= ':' or char >= 'Q':
            filtered_chars.append(char)
    return ''.join(filtered_chars)