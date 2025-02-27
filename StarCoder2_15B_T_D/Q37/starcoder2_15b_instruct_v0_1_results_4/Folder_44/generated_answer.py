def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if not (21 <= i <= 43 and '+' <= char <= '8'):
            filtered_string += char
    return filtered_string