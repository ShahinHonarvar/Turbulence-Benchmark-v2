def filter_chars(input_string):
    filtered_string = ''
    for i, char in enumerate(input_string):
        if 35 <= i <= 89 and 'E' <= char <= 't':
            continue
        filtered_string += char
    return filtered_string