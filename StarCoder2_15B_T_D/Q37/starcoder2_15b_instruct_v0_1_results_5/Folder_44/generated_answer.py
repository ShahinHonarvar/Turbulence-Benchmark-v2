def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if not (21 <= index <= 43 and '+' <= char <= '8'):
            filtered_string += char
    return filtered_string