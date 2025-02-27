def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 73 and i <= 74 and ('U' <= char <= 'l'):
            continue
        filtered_string += char
    return filtered_string