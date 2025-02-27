def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if (i >= 36 and i <= 79) and (char >= 'a' and char <= 'i'):
            continue
        filtered_string += char
    return filtered_string