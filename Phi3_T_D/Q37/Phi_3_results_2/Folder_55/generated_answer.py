def filter_chars(s):
    filtered_string = ''
    for index, char in enumerate(s[1:6]):
        if '$' <= char <= ';':
            continue
        filtered_string += char
    return filtered_string