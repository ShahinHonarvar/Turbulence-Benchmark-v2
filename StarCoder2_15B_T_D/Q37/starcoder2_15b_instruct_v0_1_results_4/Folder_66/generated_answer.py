def filter_chars(input_string):
    filtered_string = ''
    for char in input_string:
        if not (27 <= ord(char) - ord('a') <= 85 and 'c' <= char <= 'i'):
            filtered_string += char
    return filtered_string